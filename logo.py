from PIL import Image, ImageDraw

class LogoRound:

    def __init__(self, logo_filename, offset=4):
        # Open logo file.
        self.logo = Image.open(logo_filename).convert('RGBA')
        self.offset = offset
    
    def add_logo_background(self, background_fill='white'):
        # Get logo size.
        logo_w, logo_h = self.logo.size
        radius = logo_w // 2

        # Create transparent background.
        background = Image.new('RGBA', (logo_w, logo_h), (255, 255, 255, 0))

        # Calculate bounding box and reduce diameter of circle by offset.
        top_left = (0 + self.offset,  + self.offset)
        bottom_right = (logo_w - self.offset, logo_h - self.offset)
        bounding_box = [top_left, bottom_right]

        # Add non-transparent circle to background.
        ImageDraw.Draw(background).ellipse(bounding_box, fill=background_fill)

        # Overlay logo on background.
        background.paste(self.logo, (0, 0), mask=self.logo)

        self.logo = background
    
    def get_logo_size(self):
        return self.logo.size
    
    def save(self, filename):
        self.logo.save(f'./icons/{filename}')



def main():
    logo_filename = './icons/GitHub-Mark-120px-plus.png'

    logo = LogoRound(logo_filename)
    logo.add_logo_background()
    logo.save('github.png')

if __name__ == "__main__":
    main()