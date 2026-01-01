"""
Resize Agent: Creates platform-specific image variants with text overlays
"""

from typing import Dict, List
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap


class ResizeAgent:
    """
    Agent responsible for creating platform-specific image variants
    with text overlays
    """
    
    def __init__(self):
        self.agent_name = "ResizeAgent"
        
        # Platform specifications
        self.platform_specs = {
            "linkedin_landscape": {
                "size": (1200, 627),
                "platform": "LinkedIn",
                "format": "Landscape"
            },
            "instagram_portrait": {
                "size": (1080, 1350),
                "platform": "Instagram",
                "format": "Portrait"
            },
            "instagram_story": {
                "size": (1080, 1920),
                "platform": "Instagram Story",
                "format": "Story"
            },
            "facebook_landscape": {
                "size": (1200, 630),
                "platform": "Facebook",
                "format": "Landscape"
            }
        }
    
    def create_variants(
        self,
        campaign_id: str,
        image_path: str,
        headline: str,
        captions: Dict[str, str],
        layout_rules: Dict
    ) -> List[Dict]:
        """
        Create platform-specific image variants
        
        Args:
            campaign_id: Unique campaign ID
            image_path: Path to original image
            headline: Text to overlay
            captions: Platform-specific captions
            layout_rules: Layout rules from CreativeAgent
            
        Returns:
            List of creative dictionaries with paths and metadata
        """
        
        creatives = []
        
        # Create output directory
        output_dir = f"outputs/{campaign_id}"
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate each platform variant
        for variant_key, specs in self.platform_specs.items():
            try:
                output_path = self._create_variant(
                    image_path=image_path,
                    output_path=f"{output_dir}/{variant_key}.jpg",
                    target_size=specs["size"],
                    headline=headline,
                    layout_rules=layout_rules,
                    variant_key=variant_key
                )
                
                # Map platform to caption
                platform_caption_map = {
                    "linkedin_landscape": "linkedin",
                    "instagram_portrait": "instagram",
                    "instagram_story": "instagram",
                    "facebook_landscape": "facebook"
                }
                
                caption_key = platform_caption_map.get(variant_key, "facebook")
                
                creatives.append({
                    "platform": specs["platform"],
                    "format": specs["format"],
                    "size": f"{specs['size'][0]}x{specs['size'][1]}",
                    "image_url": f"/{output_path}",
                    "caption": captions.get(caption_key, ""),
                    "variant_key": variant_key
                })
                
            except Exception as e:
                print(f"Error creating variant {variant_key}: {e}")
                continue
        
        return creatives
    
    def _create_variant(
        self,
        image_path: str,
        output_path: str,
        target_size: tuple,
        headline: str,
        layout_rules: Dict,
        variant_key: str
    ) -> str:
        """
        Create a single platform variant
        """
        
        # Load and resize image
        img = Image.open(image_path)
        img = self._smart_resize(img, target_size)
        
        # Create drawing context
        draw = ImageDraw.Draw(img, "RGBA")
        
        # Get font
        font_size = layout_rules["typography"]["font_size"].get(
            variant_key,
            layout_rules["typography"]["font_size"].get("linkedin_landscape", 60)
        )
        
        try:
            # Try Windows font first
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            try:
                # Try Linux font path
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
            except:
                # Fallback to default font
                font = ImageFont.load_default()
        
        # Calculate text position
        text_bbox = draw.textbbox((0, 0), headline, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        # Position based on layout rules
        placement = layout_rules["placement"]
        padding = layout_rules["padding"]
        
        if placement["position"] == "bottom":
            y = int(target_size[1] * placement["vertical_position"])
        elif placement["position"] == "top":
            y = padding["vertical"]
        else:  # center
            y = (target_size[1] - text_height) // 2
        
        x = (target_size[0] - text_width) // 2  # Center horizontally
        
        # Draw background overlay if specified
        if layout_rules["effects"]["background_overlay"]:
            bg_color = layout_rules["colors"]["background_color"]
            bg_padding = 20
            overlay_box = [
                x - bg_padding,
                y - bg_padding,
                x + text_width + bg_padding,
                y + text_height + bg_padding
            ]
            draw.rectangle(overlay_box, fill=bg_color)
        
        # Draw text shadow if specified
        if layout_rules["effects"]["text_shadow"]:
            shadow_color = layout_rules["colors"]["shadow_color"]
            shadow_offset = 3
            draw.text(
                (x + shadow_offset, y + shadow_offset),
                headline,
                font=font,
                fill=shadow_color
            )
        
        # Draw main text
        text_color = layout_rules["colors"]["text_color"]
        draw.text((x, y), headline, font=font, fill=text_color)
        
        # Draw outline if specified
        if layout_rules["effects"]["outline"]:
            outline_color = layout_rules["colors"]["outline_color"]
            for adj_x in [-2, -1, 0, 1, 2]:
                for adj_y in [-2, -1, 0, 1, 2]:
                    if adj_x != 0 or adj_y != 0:
                        draw.text(
                            (x + adj_x, y + adj_y),
                            headline,
                            font=font,
                            fill=outline_color
                        )
            # Redraw main text on top
            draw.text((x, y), headline, font=font, fill=text_color)
        
        # Save image
        img.save(output_path, "JPEG", quality=95)
        
        return output_path
    
    def _smart_resize(self, img: Image.Image, target_size: tuple) -> Image.Image:
        """
        Resize image to target size while maintaining aspect ratio
        Uses smart cropping to focus on center
        """
        target_width, target_height = target_size
        target_ratio = target_width / target_height
        
        img_width, img_height = img.size
        img_ratio = img_width / img_height
        
        if img_ratio > target_ratio:
            # Image is wider, crop width
            new_width = int(img_height * target_ratio)
            left = (img_width - new_width) // 2
            img = img.crop((left, 0, left + new_width, img_height))
        else:
            # Image is taller, crop height
            new_height = int(img_width / target_ratio)
            top = (img_height - new_height) // 2
            img = img.crop((0, top, img_width, top + new_height))
        
        # Resize to exact target size
        img = img.resize(target_size, Image.Resampling.LANCZOS)
        
        return img