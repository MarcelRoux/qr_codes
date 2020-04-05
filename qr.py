import qrcode
from qrcode.constants import ERROR_CORRECT_Q

class QR:

    def __init__(self, data, box_size=10, border=4,
                 error_correction=ERROR_CORRECT_Q, version=None):
        self.code = qrcode.QRCode(
            version=version,
            error_correction=error_correction,
            box_size=box_size,
            border=border
        )

        self.code.add_data(data)
    
    def make(self, fit=True):
        self.code.make(fit=fit)
        self.img = self.code.make_image(fill_color='black', back_color='white')

    def save(self, filename):
        self.img.save(filename)

def main():

    qr = QR('This is some text data.')
    qr.make()
    qr.save('./out/sample.png')

if __name__ == "__main__":
    main()