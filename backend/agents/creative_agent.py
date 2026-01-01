"""
Creative Agent: Designs text overlay layout and styling rules
"""

from typing import Dict
from PIL import Image
import colorsys


class CreativeAgent:
    """
    Agent responsible for designing text overlay layout,
    positioning, and styling rules
    """
    
    def __init__(self):
        self.agent_name = "CreativeAgent"
    
    def design_layout(self, brief: Dict, headline: str) -> Dict:
        """
        Design layout rules for text overlay on image
        
        Args:
            brief: Campaign brief
            headline: Selected headline text
            
        Returns:
            Layout rules including position, font, color, effects
        """
        
        tone = brief["brand"]["tone"]
        image_path = brief["product"]["image_path"]
        
        # Analyze image to determine best text placement
        placement = self._determine_placement(image_path)
        
        # Get tone-specific styling
        styling = self._get_tone_styling(tone)
        
        # Calculate font sizes based on headline length
        font_sizes = self._calculate_font_sizes(headline)
        
        # Determine color scheme for readability
        colors = self._determine_colors(image_path, placement)
        
        layout_rules = {
            "placement": placement,
            "typography": {
                "font_family": styling["font_family"],
                "font_size": font_sizes,
                "font_weight": styling["font_weight"],
                "letter_spacing": styling["letter_spacing"],
                "line_height": 1.2
            },
            "colors": colors,
            "effects": {
                "background_overlay": styling["background_overlay"],
                "text_shadow": styling["text_shadow"],
                "outline": styling["outline"]
            },
            "padding": {
                "horizontal": 50,
                "vertical": 40
            },
            "max_width_percent": 80,
            "agent": self.agent_name
        }
        
        return layout_rules
    
    def _determine_placement(self, image_path: str) -> Dict:
        """
        Analyze image to determine best text placement
        """
        try:
            img = Image.open(image_path)
            width, height = img.size
            
            # Analyze image brightness in different regions
            # For simplicity, place text in bottom third (common pattern)
            # In production, would use image analysis to find optimal area
            
            return {
                "position": "bottom",
                "alignment": "center",
                "vertical_position": 0.75,  # 75% down from top
                "justification": "center"
            }
        except Exception as e:
            print(f"Error analyzing image: {e}")
            return {
                "position": "bottom",
                "alignment": "center",
                "vertical_position": 0.75,
                "justification": "center"
            }
    
    def _get_tone_styling(self, tone: str) -> Dict:
        """
        Get styling rules based on brand tone
        """
        tone_styles = {
            "premium": {
                "font_family": "Arial",  # In production, use premium fonts
                "font_weight": "bold",
                "letter_spacing": 2,
                "background_overlay": True,
                "text_shadow": False,
                "outline": False
            },
            "playful": {
                "font_family": "Arial",
                "font_weight": "bold",
                "letter_spacing": 0,
                "background_overlay": True,
                "text_shadow": True,
                "outline": True
            },
            "minimal": {
                "font_family": "Arial",
                "font_weight": "normal",
                "letter_spacing": 1,
                "background_overlay": False,
                "text_shadow": True,
                "outline": False
            },
            "luxury": {
                "font_family": "Arial",
                "font_weight": "bold",
                "letter_spacing": 3,
                "background_overlay": True,
                "text_shadow": False,
                "outline": False
            },
            "professional": {
                "font_family": "Arial",
                "font_weight": "bold",
                "letter_spacing": 1,
                "background_overlay": True,
                "text_shadow": False,
                "outline": False
            }
        }
        
        return tone_styles.get(tone, tone_styles["professional"])
    
    def _calculate_font_sizes(self, headline: str) -> Dict:
        """
        Calculate appropriate font sizes based on headline length
        """
        text_length = len(headline)
        
        # Base sizes for different platforms
        if text_length < 20:
            base_size = 72
        elif text_length < 40:
            base_size = 60
        else:
            base_size = 48
        
        return {
            "linkedin_landscape": base_size,
            "instagram_portrait": int(base_size * 0.9),
            "instagram_story": int(base_size * 1.2),
            "facebook_landscape": base_size
        }
    
    def _determine_colors(self, image_path: str, placement: Dict) -> Dict:
        """
        Determine text and background colors for readability
        """
        try:
            img = Image.open(image_path)
            
            # Sample colors from placement area
            # For simplicity, using standard high-contrast colors
            # In production, would analyze image colors
            
            return {
                "text_color": (255, 255, 255),  # White
                "background_color": (0, 0, 0, 180),  # Semi-transparent black
                "outline_color": (0, 0, 0),  # Black
                "shadow_color": (0, 0, 0, 128)  # Semi-transparent black
            }
        except Exception as e:
            print(f"Error determining colors: {e}")
            return {
                "text_color": (255, 255, 255),
                "background_color": (0, 0, 0, 180),
                "outline_color": (0, 0, 0),
                "shadow_color": (0, 0, 0, 128)
            }
    
    def validate_layout(self, layout_rules: Dict) -> bool:
        """
        Validate layout rules have all required fields
        """
        required_fields = ["placement", "typography", "colors", "effects"]
        return all(field in layout_rules for field in required_fields)