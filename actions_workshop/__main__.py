from PIL import Image, ImageDraw, ImageFont
import os

def add_version_text(image_path, version):
    # Load the image
    image = Image.open(image_path)
    
    # Create a new image with additional space at the bottom for the version text
    new_height = image.height  # Adjust as needed
    new_image = Image.new('RGBA', (image.width, new_height), color=(255, 255, 255, 0))
    new_image.paste(image, (0, 0))
    
    # Add the version text
    draw = ImageDraw.Draw(new_image)
    font_size = 100
    font = ImageFont.truetype("font.ttf", font_size)
    text = f"Version: {version}"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    print(f"Text width: {text_width}, Text height: {text_height}")
    print(f"Image width: {image.width}, Image height: {image.height}")
    x = (image.width - text_width) // 2  # Adjust as needed
    y = image.height - 150  # Adjust as needed

    text_color = (255, 255, 255, 255)  # White color
    draw.text((x, y), text, fill=text_color, font=font)  

    # Save the modified image
    base_path, ext = os.path.splitext(image_path)
    output_path = "logo.png" 
    new_image.save(output_path)
    
    print(f"Version text added. Image saved to: {output_path}")

# Call this using `python -m actions_workshop` and `$ actions_workshop `.
if __name__ == "__main__":
    # Path to the logo image
    logo_path = "logo_base.png"
    
    # Load the version from the VERSION file
    with open('VERSION', 'r') as f:
        version = f.read().strip()
    
    # Add version to image
    add_version_text(logo_path, version)
