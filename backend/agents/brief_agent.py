"""
Brief Agent: Converts user inputs into structured campaign brief
"""

from typing import List, Dict
from datetime import datetime
import json


class BriefAgent:
    """
    Agent responsible for creating structured campaign briefs
    from raw user inputs
    """
    
    def __init__(self):
        self.agent_name = "BriefAgent"
    
    def create_brief(
        self,
        campaign_id: str,
        product_name: str,
        features: List[str],
        tone: str,
        image_path: str
    ) -> Dict:
        """
        Create a structured campaign brief
        
        Args:
            campaign_id: Unique campaign identifier
            product_name: Name of the product
            features: List of key product features
            tone: Brand tone (premium, playful, minimal, luxury, professional)
            image_path: Path to uploaded product image
            
        Returns:
            Structured brief as JSON
        """
        
        # Validate inputs
        if not product_name:
            raise ValueError("Product name is required")
        
        if not features or len(features) < 3:
            raise ValueError("At least 3 features are required")
        
        # Clean features
        clean_features = [f.strip() for f in features if f.strip()]
        
        # Create structured brief
        brief = {
            "campaign_id": campaign_id,
            "product": {
                "name": product_name,
                "features": clean_features,
                "image_path": image_path
            },
            "brand": {
                "tone": tone,
                "voice_attributes": self._get_tone_attributes(tone)
            },
            "platforms": {
                "linkedin": {
                    "format": "professional",
                    "max_caption_length": 3000,
                    "hashtag_count": "3-5",
                    "image_sizes": ["1200x627"]
                },
                "instagram": {
                    "format": "visual_storytelling",
                    "max_caption_length": 2200,
                    "hashtag_count": "10-15",
                    "image_sizes": ["1080x1350", "1080x1920"]
                },
                "facebook": {
                    "format": "engaging",
                    "max_caption_length": 63206,
                    "hashtag_count": "2-3",
                    "image_sizes": ["1200x630"]
                }
            },
            "objectives": [
                "Generate brand awareness",
                "Highlight key product features",
                "Drive engagement and conversions"
            ],
            "created_at": datetime.now().isoformat(),
            "agent": self.agent_name
        }
        
        return brief
    
    def _get_tone_attributes(self, tone: str) -> Dict:
        """
        Map tone to specific voice attributes
        """
        tone_mapping = {
            "premium": {
                "adjectives": ["sophisticated", "refined", "quality"],
                "style": "Elegant and authoritative",
                "avoid": ["slang", "emojis", "exclamation marks"]
            },
            "playful": {
                "adjectives": ["fun", "energetic", "vibrant"],
                "style": "Light-hearted and engaging",
                "avoid": ["formal language", "technical jargon"]
            },
            "minimal": {
                "adjectives": ["simple", "clean", "essential"],
                "style": "Concise and focused",
                "avoid": ["flowery language", "excessive details"]
            },
            "luxury": {
                "adjectives": ["exclusive", "prestigious", "exceptional"],
                "style": "Aspirational and refined",
                "avoid": ["common phrases", "mass market language"]
            },
            "professional": {
                "adjectives": ["reliable", "trustworthy", "expert"],
                "style": "Clear and authoritative",
                "avoid": ["casual language", "informal tone"]
            }
        }
        
        return tone_mapping.get(tone, tone_mapping["professional"])
    
    def validate_brief(self, brief: Dict) -> bool:
        """
        Validate that brief has all required fields
        """
        required_fields = ["campaign_id", "product", "brand", "platforms"]
        return all(field in brief for field in required_fields)