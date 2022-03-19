from qr import QR
from logo import LogoRound
import json


with open('./data.json', 'r') as f:
    resources = json.load(f)


def main():

    for name, resource in resources.items():
        # Logo section.
        logo = LogoRound(resource['logo'])
        if('add_logo_background' in resource and resource['add_logo_background'] == True):
            logo.add_logo_background(resource['logo_background_fill'])
        logo.save(resource['logo_filename'])

        # QR section.
        qr = QR(resource['url'], box_size=resource['box_size'], border=2)
        qr.make(fit=True, fill_color=resource['colour'])
        qr.add_logo(logo.img)
        qr.save(resource['qr_filename'])

if __name__ == "__main__":
    main()