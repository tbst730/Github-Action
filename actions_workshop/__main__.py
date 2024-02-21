import argparse
from PIL import Image, ImageDraw, ImageFont

def add_version_text(version, base_logo, new_logo):
    # Load the image
    image = Image.open(base_logo)
    
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
    x = (image.width - text_width) // 2  # Adjust as needed
    y = image.height - 150  # Adjust as needed

    text_color = (255, 255, 255, 255)  # White color
    draw.text((x, y), text, fill=text_color, font=font)  

    # Save the modified image
    output_path = new_logo 
    new_image.save(output_path)
    
    print(f"Version text added. Image saved to: {output_path}")

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description='Add version text to logo image')
    
    # Add arguments
    parser.add_argument('--version', dest='version', type=str, help='Path to the version file')
    parser.add_argument('--base-logo', dest='base_logo', type=str, help='Path to the base logo image')
    parser.add_argument('--new-logo', dest='new_logo', type=str, help='Path to save the new logo image')
    
    # Parse arguments
    args = parser.parse_args()

    # Load the version from the VERSION file
    with open(args.version, 'r') as f:
        version = f.read().strip()
    
    # Call main function with arguments
    add_version_text(version, args.base_logo, args.new_logo)
