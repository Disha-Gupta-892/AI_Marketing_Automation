"""
Publisher Agent: Posts content to social media platforms
"""

from typing import Dict, List
import os
import requests
from datetime import datetime


class PublisherAgent:
    """
    Agent responsible for publishing content to social media platforms
    """
    
    def __init__(self):
        self.agent_name = "PublisherAgent"
        
        # Load API credentials from environment
        self.linkedin_token = os.getenv("LINKEDIN_ACCESS_TOKEN")
        self.facebook_token = os.getenv("FACEBOOK_ACCESS_TOKEN")
        self.facebook_page_id = os.getenv("FACEBOOK_PAGE_ID")
        self.instagram_user_id = os.getenv("INSTAGRAM_USER_ID")
        self.instagram_token = os.getenv("INSTAGRAM_ACCESS_TOKEN")
    
    def publish(
        self,
        campaign_id: str,
        creatives: List[Dict],
        platforms: List[str] = None
    ) -> List[Dict]:
        """
        Publish creatives to specified platforms
        
        Args:
            campaign_id: Unique campaign ID
            creatives: List of creative dictionaries
            platforms: List of platforms to publish to
            
        Returns:
            List of publish results
        """
        
        if platforms is None:
            platforms = ["linkedin", "facebook"]
        
        results = []
        
        for platform in platforms:
            if platform.lower() == "linkedin":
                result = self._publish_to_linkedin(campaign_id, creatives)
                results.append(result)
            elif platform.lower() == "facebook":
                result = self._publish_to_facebook(campaign_id, creatives)
                results.append(result)
            elif platform.lower() == "instagram":
                result = self._publish_to_instagram(campaign_id, creatives)
                results.append(result)
        
        return results
    
    def _publish_to_linkedin(self, campaign_id: str, creatives: List[Dict]) -> Dict:
        """
        Publish to LinkedIn
        """
        
        # Find LinkedIn creative
        linkedin_creative = next(
            (c for c in creatives if "LinkedIn" in c["platform"]),
            None
        )
        
        if not linkedin_creative:
            return {
                "platform": "linkedin",
                "success": False,
                "message": "No LinkedIn creative found"
            }
        
        # Check if token is available
        if not self.linkedin_token:
            return {
                "platform": "linkedin",
                "success": False,
                "message": "LinkedIn API token not configured. Set LINKEDIN_ACCESS_TOKEN environment variable.",
                "demo_mode": True,
                "simulated_url": f"https://linkedin.com/feed/update/urn:li:share:{campaign_id}"
            }
        
        try:
            # In production, use LinkedIn API to post
            # For demo, simulate the post
            
            # LinkedIn API endpoint
            url = "https://api.linkedin.com/v2/ugcPosts"
            
            headers = {
                "Authorization": f"Bearer {self.linkedin_token}",
                "Content-Type": "application/json",
                "X-Restli-Protocol-Version": "2.0.0"
            }
            
            # Prepare post data
            post_data = {
                "author": f"urn:li:person:{self.linkedin_token}",  # Replace with actual person URN
                "lifecycleState": "PUBLISHED",
                "specificContent": {
                    "com.linkedin.ugc.ShareContent": {
                        "shareCommentary": {
                            "text": linkedin_creative["caption"]
                        },
                        "shareMediaCategory": "IMAGE",
                        "media": [
                            {
                                "status": "READY",
                                "description": {
                                    "text": "Marketing creative"
                                },
                                "media": f"urn:li:digitalmediaAsset:{campaign_id}",
                                "title": {
                                    "text": "Product Marketing"
                                }
                            }
                        ]
                    }
                },
                "visibility": {
                    "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
                }
            }
            
            # For demo purposes, simulate success
            return {
                "platform": "linkedin",
                "success": True,
                "message": "Successfully posted to LinkedIn (Demo Mode)",
                "post_url": f"https://linkedin.com/feed/update/urn:li:share:{campaign_id}",
                "posted_at": datetime.now().isoformat(),
                "demo_mode": True
            }
            
        except Exception as e:
            return {
                "platform": "linkedin",
                "success": False,
                "message": f"Error: {str(e)}",
                "demo_mode": True
            }
    
    def _publish_to_facebook(self, campaign_id: str, creatives: List[Dict]) -> Dict:
        """
        Publish to Facebook
        """
        
        # Find Facebook creative
        facebook_creative = next(
            (c for c in creatives if c["platform"] == "Facebook"),
            None
        )
        
        if not facebook_creative:
            return {
                "platform": "facebook",
                "success": False,
                "message": "No Facebook creative found"
            }
        
        # Check if token is available
        if not self.facebook_token or not self.facebook_page_id:
            return {
                "platform": "facebook",
                "success": False,
                "message": "Facebook API credentials not configured. Set FACEBOOK_ACCESS_TOKEN and FACEBOOK_PAGE_ID.",
                "demo_mode": True,
                "simulated_url": f"https://facebook.com/{self.facebook_page_id}/posts/{campaign_id}"
            }
        
        try:
            # In production, use Facebook Graph API
            # For demo, simulate the post
            
            # Facebook Graph API endpoint
            url = f"https://graph.facebook.com/v18.0/{self.facebook_page_id}/photos"
            
            # Prepare post data
            post_data = {
                "message": facebook_creative["caption"],
                "access_token": self.facebook_token
            }
            
            # For demo purposes, simulate success
            return {
                "platform": "facebook",
                "success": True,
                "message": "Successfully posted to Facebook (Demo Mode)",
                "post_url": f"https://facebook.com/{campaign_id}",
                "posted_at": datetime.now().isoformat(),
                "demo_mode": True
            }
            
        except Exception as e:
            return {
                "platform": "facebook",
                "success": False,
                "message": f"Error: {str(e)}",
                "demo_mode": True
            }
    
    def _publish_to_instagram(self, campaign_id: str, creatives: List[Dict]) -> Dict:
        """
        Publish to Instagram
        """
        
        # Find Instagram creative
        instagram_creative = next(
            (c for c in creatives if "Instagram" in c["platform"] and c["format"] == "Portrait"),
            None
        )
        
        if not instagram_creative:
            return {
                "platform": "instagram",
                "success": False,
                "message": "No Instagram creative found"
            }
        
        # Check if token is available
        if not self.instagram_token or not self.instagram_user_id:
            return {
                "platform": "instagram",
                "success": False,
                "message": "Instagram API credentials not configured. Set INSTAGRAM_ACCESS_TOKEN and INSTAGRAM_USER_ID.",
                "demo_mode": True,
                "simulated_url": f"https://instagram.com/p/{campaign_id}"
            }
        
        try:
            # In production, use Instagram Graph API
            # For demo, simulate the post
            
            return {
                "platform": "instagram",
                "success": True,
                "message": "Successfully posted to Instagram (Demo Mode)",
                "post_url": f"https://instagram.com/p/{campaign_id}",
                "posted_at": datetime.now().isoformat(),
                "demo_mode": True
            }
            
        except Exception as e:
            return {
                "platform": "instagram",
                "success": False,
                "message": f"Error: {str(e)}",
                "demo_mode": True
            }