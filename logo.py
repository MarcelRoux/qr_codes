from PIL import Image, ImageDraw

def main():
    logo_filename = './icons/GitHub-Mark-120px-plus.png'

    # Open logo and get size.
    logo = Image.open(logo_filename).convert('RGBA')
    logo_w, logo_h = logo.size
    radius = logo_w // 2

    # Create transparent background.
    background = Image.new('RGBA', (logo_w, logo_h), (255, 255, 255, 0))

    # Reduce diameter of circle by offset.
    offset = 4

    # Calculate bounding box.
    top_left = (0 + offset, 0 + offset)
    bottom_right = (logo_w - 1 - offset, logo_h - 1 - offset)
    bounding_box = [top_left, bottom_right] 
    
    # Add circle to background.
    ImageDraw.Draw(background).ellipse(bounding_box, fill='white')
    
    # Overlay logo on background.
    background.paste(logo, (0, 0), mask=logo) 
    background.save('./icons/github.png')

if __name__ == "__main__":
    main()