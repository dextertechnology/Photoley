import argparse
import os

from configparser import ConfigParser

import photoley
from photos.photos import Photos


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UNSPLASH_URL = 'https://source.unsplash.com'
MEDIA_DIR = os.path.join(BASE_DIR, 'media')


def main():
    parser = argparse.ArgumentParser(
        prog='photoley',
        usage='%(prog)s [options]',
        description="Using unsplash, fetch random wallpaper with specific size and category.",
        epilog='Enjoy the Photoley')

    parser.add_argument('-v',
        '--version',
        help="Check version",
        action="version",
        version=f'%(prog)s {photoley.__version__}'
    )
    parser.add_argument('-q', '--query', metavar='', type=str, help="Comma-separated string search query to get relevant random image")
    parser.add_argument('-r', '--resolution', metavar='', type=str, help="Resolution of screen. eg: 1920x1080, 1366x768")
    parser.add_argument('-u', '--user', metavar='', type=str, help="Username that exists in unsplash eg: erondu")
    parser.add_argument('-c', '--collection', metavar='', type=int, help="Integer: Collection that exists in unsplash eg: 190727")

    args = parser.parse_args()

    cfg = ConfigParser()
    cfg.read(os.path.join(BASE_DIR, 'config.ini'))

    global UNSPLASH_URL, MEDIA_DIR

    try:
        UNSPLASH_URL = cfg.get("photoley", "url")
    except Exception:
        print("No config found for url. \
            \nDefault value is set instead.")
    
    try:
        MEDIA_DIR = cfg.get("photoley", "media_dir")
    except Exception:
        print("No config found for media_dir. \
            \nDefault value is set instead.")

    p = Photos(args=args, url=UNSPLASH_URL, dir=MEDIA_DIR)
    p.save()


if __name__ == "__main__":
    main()
