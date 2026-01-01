"""
Campaign storage utility for persisting campaign data
"""

import json
import os
from typing import Dict, List, Optional
from datetime import datetime


class CampaignStorage:
    """
    Simple file-based storage for campaign data
    In production, would use a database
    """
    
    def __init__(self, storage_dir: str = "campaign_data"):
        self.storage_dir = storage_dir
        os.makedirs(storage_dir, exist_ok=True)
    
    def save_campaign(self, campaign_id: str, data: Dict) -> bool:
        """
        Save campaign data to file
        
        Args:
            campaign_id: Unique campaign identifier
            data: Campaign data dictionary
            
        Returns:
            True if successful
        """
        try:
            file_path = os.path.join(self.storage_dir, f"{campaign_id}.json")
            
            # Add metadata
            data["last_updated"] = datetime.now().isoformat()
            
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
            
            return True
        except Exception as e:
            print(f"Error saving campaign {campaign_id}: {e}")
            return False
    
    def load_campaign(self, campaign_id: str) -> Optional[Dict]:
        """
        Load campaign data from file
        
        Args:
            campaign_id: Unique campaign identifier
            
        Returns:
            Campaign data dictionary or None if not found
        """
        try:
            file_path = os.path.join(self.storage_dir, f"{campaign_id}.json")
            
            if not os.path.exists(file_path):
                return None
            
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            return data
        except Exception as e:
            print(f"Error loading campaign {campaign_id}: {e}")
            return None
    
    def list_campaigns(self) -> List[Dict]:
        """
        List all campaigns with basic metadata
        
        Returns:
            List of campaign metadata
        """
        campaigns = []
        
        try:
            for filename in os.listdir(self.storage_dir):
                if filename.endswith('.json'):
                    campaign_id = filename.replace('.json', '')
                    file_path = os.path.join(self.storage_dir, filename)
                    
                    with open(file_path, 'r') as f:
                        data = json.load(f)
                    
                    campaigns.append({
                        "campaign_id": campaign_id,
                        "product_name": data.get("brief", {}).get("product", {}).get("name", "Unknown"),
                        "status": data.get("status", "unknown"),
                        "created_at": data.get("created_at"),
                        "last_updated": data.get("last_updated")
                    })
            
            # Sort by created_at descending
            campaigns.sort(key=lambda x: x.get("created_at", ""), reverse=True)
            
        except Exception as e:
            print(f"Error listing campaigns: {e}")
        
        return campaigns
    
    def delete_campaign(self, campaign_id: str) -> bool:
        """
        Delete campaign data
        
        Args:
            campaign_id: Unique campaign identifier
            
        Returns:
            True if successful
        """
        try:
            file_path = os.path.join(self.storage_dir, f"{campaign_id}.json")
            
            if os.path.exists(file_path):
                os.remove(file_path)
                return True
            
            return False
        except Exception as e:
            print(f"Error deleting campaign {campaign_id}: {e}")
            return False
    
    def update_campaign_status(self, campaign_id: str, status: str) -> bool:
        """
        Update campaign status
        
        Args:
            campaign_id: Unique campaign identifier
            status: New status
            
        Returns:
            True if successful
        """
        data = self.load_campaign(campaign_id)
        if data:
            data["status"] = status
            return self.save_campaign(campaign_id, data)
        return False