from PIL import Image, ImageDraw


class LogoRound:

    def __init__(self, logo_filename, offset=4):
        # Open logo file.
        self.img = Image.open(logo_filename).convert('RGBA')
        self.offset = offset

    def add_logo_background(self, background_fill='white'):
        # Get logo size.
        img_w, img_h = self.img.size
        radius = img_w // 2

        # Calculate bounding box and reduce diameter of circle by offset.
        top_left = (0, 0)
        bottom_right = (img_w - self.offset, img_h - self.offset)
        bounding_box = [top_left, bottom_right]

        # Create transparent background.
        background = Image.new('RGBA',
                               (bottom_right[0], bottom_right[1]),
                               (255, 255, 255, 0))

        # Add non-transparent circle to background.
        ImageDraw.Draw(background).ellipse(bounding_box, fill=background_fill)

        # Overlay logo on background.
        background.paste(self.img,
                         (-self.offset//2, -self.offset//2),
                         mask=self.img)

        self.img = background

    def get_logo_size(self):
        return self.img.size

    def save(self, filename):
        self.img.save(f'./icons/{filename}')


def create_github_logo():
    logo_filename = './icons/GitHub-Mark-120px-plus.png'

    logo = LogoRound(logo_filename)
    logo.add_logo_background()
    logo.save('github.png')


def create_mail_logo():
    logo_filename = './icons/mail_sample.png'

    logo = LogoRound(logo_filename, offset=-72)
    logo.add_logo_background()
    logo.save('mail.png')


def main():
    create_github_logo()
    create_mail_logo()


if __name__ == "__main__":
    main()
