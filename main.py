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
        'logo_background_fill': 'white',
        'box_size': 8
    },
    'linked_in': {
        'qr_filename': 'linkedin.png',
        'logo_filename': 'linkedin.png',
        'logo': './icons/linkedin_logo_512.png',
        'url': 'https://www.linkedin.com/in/rouxmarcel/',
        'colour': '#0077B5',
        # 'add_logo_background': True,
        # 'logo_background_fill': 'white',
        'box_size': 32
    }
}

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