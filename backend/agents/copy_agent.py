"""
Copy Agent: Generates marketing headlines and captions using AI
"""

import os
from typing import Dict, List
import openai
from openai import OpenAI
import json


class CopyAgent:
    """
    Agent responsible for generating marketing copy
    using OpenAI GPT-4
    """
    
    def __init__(self):
        self.agent_name = "CopyAgent"
        # Initialize OpenAI client
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or api_key == "sk-your-openai-api-key-here":
            # Allow initialization without key, but will fail at runtime
            self.client = None
            self.api_key_missing = True
        else:
            self.client = OpenAI(api_key=api_key)
            self.api_key_missing = False
        self.model = "gpt-4-turbo-preview"
    
    def generate_copy(self, brief: Dict) -> Dict:
        """
        Generate headlines and platform-specific captions
        
        Args:
            brief: Structured campaign brief from BriefAgent
            
        Returns:
            Dictionary with headlines and captions
        """
        
        if self.api_key_missing or not self.client:
            raise ValueError("OPENAI_API_KEY environment variable not set. Please add your API key to backend/.env file")
        
        product_name = brief["product"]["name"]
        features = brief["product"]["features"]
        tone = brief["brand"]["tone"]
        tone_attributes = brief["brand"]["voice_attributes"]
        
        # Generate headlines
        headlines = self._generate_headlines(
            product_name, features, tone, tone_attributes
        )
        
        # Generate platform-specific captions
        captions = {
            "linkedin": self._generate_captions(
                product_name, features, tone, "linkedin", brief["platforms"]["linkedin"]
            ),
            "instagram": self._generate_captions(
                product_name, features, tone, "instagram", brief["platforms"]["instagram"]
            ),
            "facebook": self._generate_captions(
                product_name, features, tone, "facebook", brief["platforms"]["facebook"]
            )
        }
        
        return {
            "headlines": headlines,
            "captions": captions,
            "agent": self.agent_name
        }
    
    def _generate_headlines(
        self,
        product_name: str,
        features: List[str],
        tone: str,
        tone_attributes: Dict
    ) -> List[str]:
        """Generate 3 headline options for image overlay"""
        
        prompt = f"""You are an expert marketing copywriter. Generate 3 short, impactful headlines for a product image overlay.

Product: {product_name}
Key Features: {', '.join(features)}
Brand Tone: {tone} - {tone_attributes['style']}

Requirements:
- Each headline must be 3-8 words maximum
- Should be punchy and memorable
- Suitable for overlay on product image
- Must align with {tone} tone
- Avoid: {', '.join(tone_attributes['avoid'])}

Return ONLY a JSON array of 3 headlines, nothing else.
Format: ["Headline 1", "Headline 2", "Headline 3"]
"""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert marketing copywriter. Always return valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=200
            )
            
            content = response.choices[0].message.content.strip()
            # Remove markdown code blocks if present
            if content.startswith("```"):
                content = content.split("```")[1]
                if content.startswith("json"):
                    content = content[4:]
            
            headlines = json.loads(content)
            return headlines[:3]  # Ensure only 3 headlines
            
        except Exception as e:
            # Fallback headlines if API fails
            print(f"Error generating headlines: {e}")
            return [
                f"Discover {product_name}",
                f"Experience {product_name}",
                f"{product_name} - Redefined"
            ]
    
    def _generate_captions(
        self,
        product_name: str,
        features: List[str],
        tone: str,
        platform: str,
        platform_specs: Dict
    ) -> List[str]:
        """Generate 2 caption options for specific platform"""
        
        prompt = f"""You are an expert {platform} marketing specialist. Generate 2 engaging captions for this product.

Product: {product_name}
Key Features: {', '.join(features)}
Brand Tone: {tone}
Platform: {platform}
Format: {platform_specs['format']}
Max Length: {platform_specs['max_caption_length']} characters
Hashtags: Include {platform_specs['hashtag_count']} relevant hashtags

Requirements:
- Write in {tone} tone
- Optimize for {platform} audience and format
- Include call-to-action
- Add appropriate hashtags
- Keep under max length
- Make it engaging and conversion-focused

Return ONLY a JSON array of 2 captions, nothing else.
Format: ["Caption 1 with #hashtags", "Caption 2 with #hashtags"]
"""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": f"You are an expert {platform} marketing specialist. Always return valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=500
            )
            
            content = response.choices[0].message.content.strip()
            # Remove markdown code blocks if present
            if content.startswith("```"):
                content = content.split("```")[1]
                if content.startswith("json"):
                    content = content[4:]
            
            captions = json.loads(content)
            return captions[:2]  # Ensure only 2 captions
            
        except Exception as e:
            # Fallback captions if API fails
            print(f"Error generating {platform} captions: {e}")
            return [
                f"Introducing {product_name}! {features[0]}. Learn more today. #{product_name.replace(' ', '')} #Innovation",
                f"Transform your experience with {product_name}. {features[1]}. Get yours now! #{product_name.replace(' ', '')} #Quality"
            ]