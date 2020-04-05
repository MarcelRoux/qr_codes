import qrcode
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_Q

class QR:

    def __init__(self, data, box_size=10, border=4,
                 error_correction=ERROR_CORRECT_Q, version=None):
        self.code = qrcode.QRCode(
            version=version,
            error_correction=error_correction,
            box_size=box_size,
            border=border
        )

        self.data = data
    
    def make(self, fit=True, fill_color='black', back_color='white'):
        self.fit = fit
        self.fill_color = fill_color
        self.back_color = back_color

        self.code.clear()
        self.code.add_data(self.data)
        self.code.make(fit=fit)
        self.img = self.code.make_image(fill_color=fill_color, back_color=back_color)
    
    def add_logo(self, logo):
        logo = logo.convert('RGBA')

        # Adding logo reduces surface area of code.
        # To compensate, increase QR version.
        self.code.version += 3
        self.make(self.fit, self.fill_color, self.back_color)

        self.img = self.img.convert('RGBA')

        logo_w, logo_h = logo.size
        img_w, img_h = self.img.size

        offset_h = (img_h - logo_h) // 2
        offset_w = (img_w - logo_w) // 2

        self.img.paste(logo, (offset_w, offset_h), mask=logo)

    def save(self, filename):
        self.img.save(f'./out/{filename}')

def main():

    qr = QR('This is some text data.', box_size=8, border=2,
            version=5, error_correction=ERROR_CORRECT_L)
    qr.make(fit=False)
    qr.save('sample_version_5.png')

if __name__ == "__main__":
    main()