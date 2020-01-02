import argparse
import os

from . import config
from photoley.photos.photos import Photos


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
        version=f'%(prog)s {config.VERSION}'
    )   
    parser.add_argument('-q', '--query', metavar='', type=str, help="Comma-separated string search query to get relevant random image")
    parser.add_argument('-r', '--resolution', metavar='', type=str, help="Resolution of screen. eg: 1920x1080, 1366x768")
    parser.add_argument('-u', '--user', metavar='', type=str, help="Username that exists in unsplash eg: erondu")
    parser.add_argument('-c', '--collection', metavar='', type=int, help="Integer: Collection that exists in unsplash eg: 190727")

    args = parser.parse_args()

    p = Photos(args=args, url=config.UNSPLASH_URL, dir=config.MEDIA_DIR)
    p.save()
