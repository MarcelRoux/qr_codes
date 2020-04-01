import qrcode

def main():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data('This is some text data.')
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color='white')

    img.save('./out/sample.png')

if __name__ == "__main__":
    main()