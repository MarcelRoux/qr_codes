from qr import QR
from logo import LogoRound
import json


with open('./data.json', 'r') as f:
    resources = json.load(f)


def main():

    for name, resource in resources.items():
        # Logo section.
        logo = LogoRound(resource.get('logo', 'missing.png'),
                         offset=resource.get('offset', 4))
        if(resource.get('add_logo_background', False)):
            logo.add_logo_background(resource.get('logo_background_fill',
                                                  'white'))
        logo.save(resource.get('logo_filename', 'logo_out.png'))

        # QR section.
        qr = QR(resource.get('url', 'https//:example.com'),
                box_size=resource.get('box_size', 8),
                border=2)
        qr.make(fit=True, fill_color=resource.get('colour', 'white'))
        qr.add_logo(logo.img)
        qr.save(resource.get('qr_filename', 'qr_out.png'))


if __name__ == "__main__":
    main()
