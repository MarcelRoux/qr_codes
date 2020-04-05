from qr import QR
from logo import LogoRound

resources = {
    'github': {
        'qr_filename': 'github.png',
        'logo_filename': 'github.png',
        'logo': './icons/GitHub-Mark-120px-plus.png',
        'url': 'https://github.com/MarcelRoux',
        'colour': '#171516',
        'add_logo_background': True,
        'logo_background_fill': 'white'
    }
}

def main():

    for name, resource in resources.items():
        # Logo section.
        logo = LogoRound(resource['logo'])
        if('add_logo_background' in resource):
            logo.add_logo_background(resource['logo_background_fill'])
        logo.save(resource['logo_filename'])

        # QR section.
        qr = QR(resource['url'], box_size=8, border=2,)
        qr.make(fit=True, fill_color=resource['colour'])
        qr.add_logo(logo.img)
        qr.save(resource['qr_filename'])

if __name__ == "__main__":
    main()