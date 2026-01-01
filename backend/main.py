"""
AI-First Marketing Automation Backend
FastAPI server with agent-based architecture
"""

from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Dict, Optional
import json
import uuid
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from agents.brief_agent import BriefAgent
from agents.copy_agent import CopyAgent
from agents.creative_agent import CreativeAgent
from agents.resize_agent import ResizeAgent
from agents.publisher_agent import PublisherAgent
from utils.logger import setup_logger
from utils.storage import CampaignStorage

# Initialize FastAPI app
app = FastAPI(title="AI Marketing Automation API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup directories
os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# Mount static files
app.mount("/outputs", StaticFiles(directory="outputs"), name="outputs")

# Initialize logger and storage
logger = setup_logger()
storage = CampaignStorage()

# Initialize agents
brief_agent = BriefAgent()
copy_agent = CopyAgent()
creative_agent = CreativeAgent()
resize_agent = ResizeAgent()
publisher_agent = PublisherAgent()


# Pydantic models
class GenerateCopyRequest(BaseModel):
    product_name: str
    features: List[str]
    tone: str


class CreateCreativesRequest(BaseModel):
    campaign_id: str
    selected_headline: int
    selected_captions: Dict[str, int]


class PublishRequest(BaseModel):
    campaign_id: str
    platforms: Optional[List[str]] = ["linkedin", "facebook"]


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "online",
        "service": "AI Marketing Automation API",
        "version": "1.0.0"
    }


@app.post("/api/generate-copy")
async def generate_copy(
    image: UploadFile = File(...),
    product_name: str = Form(...),
    features: str = Form(...),
    tone: str = Form(...)
):
    """
    Step 1: Upload image and generate marketing copy
    
    Flow:
    1. Brief Agent: Create structured campaign brief
    2. Copy Agent: Generate headlines and captions
    3. Return options for user review
    """
    try:
        campaign_id = str(uuid.uuid4())
        logger.info(f"Starting campaign {campaign_id}")
        
        # Save uploaded image
        image_path = f"uploads/{campaign_id}_{image.filename}"
        with open(image_path, "wb") as f:
            f.write(await image.read())
        
        # Parse features
        features_list = json.loads(features)
        
        # AGENT 1: Brief Agent - Create structured brief
        logger.info("Agent 1: Brief Agent creating campaign brief...")
        brief = brief_agent.create_brief(
            campaign_id=campaign_id,
            product_name=product_name,
            features=features_list,
            tone=tone,
            image_path=image_path
        )
        logger.info(f"Brief created: {json.dumps(brief, indent=2)}")
        
        # AGENT 2: Copy Agent - Generate marketing copy
        logger.info("Agent 2: Copy Agent generating copy...")
        copy_content = copy_agent.generate_copy(brief)
        logger.info(f"Generated {len(copy_content['headlines'])} headlines and captions for {len(copy_content['captions'])} platforms")
        
        # Store campaign data
        campaign_data = {
            "campaign_id": campaign_id,
            "brief": brief,
            "copy_content": copy_content,
            "image_path": image_path,
            "created_at": datetime.now().isoformat(),
            "status": "copy_generated"
        }
        storage.save_campaign(campaign_id, campaign_data)
        
        return {
            "campaign_id": campaign_id,
            "headlines": copy_content["headlines"],
            "captions": copy_content["captions"],
            "brief": brief
        }
        
    except Exception as e:
        logger.error(f"Error in generate_copy: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/create-creatives")
async def create_creatives(request: CreateCreativesRequest):
    """
    Step 2: User approves copy, create platform-specific creatives
    
    Flow:
    1. Creative Agent: Design text overlay with placement rules
    2. Resize Agent: Generate platform-specific sizes
    3. Return creative previews
    """
    try:
        campaign_id = request.campaign_id
        logger.info(f"Creating creatives for campaign {campaign_id}")
        
        # Load campaign data
        campaign_data = storage.load_campaign(campaign_id)
        if not campaign_data:
            raise HTTPException(status_code=404, detail="Campaign not found")
        
        brief = campaign_data["brief"]
        copy_content = campaign_data["copy_content"]
        
        # Get selected content
        selected_headline = copy_content["headlines"][request.selected_headline]
        selected_captions = {
            platform: copy_content["captions"][platform][caption_idx]
            for platform, caption_idx in request.selected_captions.items()
        }
        
        # AGENT 3: Creative Agent - Design overlay
        logger.info("Agent 3: Creative Agent designing overlay...")
        layout_rules = creative_agent.design_layout(
            brief=brief,
            headline=selected_headline
        )
        logger.info(f"Layout rules: {json.dumps(layout_rules, indent=2)}")
        
        # AGENT 4: Resize Agent - Create platform variants
        logger.info("Agent 4: Resize Agent creating platform variants...")
        creatives = resize_agent.create_variants(
            campaign_id=campaign_id,
            image_path=campaign_data["image_path"],
            headline=selected_headline,
            captions=selected_captions,
            layout_rules=layout_rules
        )
        logger.info(f"Created {len(creatives)} platform variants")
        
        # Update campaign data
        campaign_data["selected_content"] = {
            "headline": selected_headline,
            "captions": selected_captions,
            "layout_rules": layout_rules
        }
        campaign_data["creatives"] = creatives
        campaign_data["status"] = "creatives_ready"
        storage.save_campaign(campaign_id, campaign_data)
        
        return {
            "campaign_id": campaign_id,
            "creatives": creatives,
            "message": "Creatives generated successfully"
        }
        
    except Exception as e:
        logger.error(f"Error in create_creatives: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/publish")
async def publish_to_platforms(request: PublishRequest):
    """
    Step 3: Publish approved creatives to social media platforms
    
    Flow:
    1. Publisher Agent: Post to each platform
    2. Return publish status and URLs
    """
    try:
        campaign_id = request.campaign_id
        logger.info(f"Publishing campaign {campaign_id}")
        
        # Load campaign data
        campaign_data = storage.load_campaign(campaign_id)
        if not campaign_data:
            raise HTTPException(status_code=404, detail="Campaign not found")
        
        if "creatives" not in campaign_data:
            raise HTTPException(status_code=400, detail="Creatives not created yet")
        
        # AGENT 5: Publisher Agent - Publish to platforms
        logger.info("Agent 5: Publisher Agent publishing content...")
        publish_results = publisher_agent.publish(
            campaign_id=campaign_id,
            creatives=campaign_data["creatives"],
            platforms=request.platforms
        )
        logger.info(f"Published to {len(publish_results)} platforms")
        
        # Update campaign data
        campaign_data["publish_results"] = publish_results
        campaign_data["status"] = "published"
        campaign_data["published_at"] = datetime.now().isoformat()
        storage.save_campaign(campaign_id, campaign_data)
        
        return {
            "campaign_id": campaign_id,
            "results": publish_results,
            "message": "Publishing completed"
        }
        
    except Exception as e:
        logger.error(f"Error in publish: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/campaign/{campaign_id}")
async def get_campaign(campaign_id: str):
    """Get campaign details"""
    campaign_data = storage.load_campaign(campaign_id)
    if not campaign_data:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return campaign_data


@app.get("/api/campaigns")
async def list_campaigns():
    """List all campaigns"""
    campaigns = storage.list_campaigns()
    return {"campaigns": campaigns}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)