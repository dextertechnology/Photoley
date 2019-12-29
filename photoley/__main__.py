import argparse
import string
import os

from configparser import ConfigParser
from enum import Enum

import photoley


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UNSPLASH_URL = 'https://source.unsplash.com/random'

def check_case(arg):
    _lcase = string.ascii_lowercase
    for a in arg:
        if not a in _lcase:
            raise Exception("Supply all string in lowercase with no symbols")

class Resolution(str, Enum):
    hd = "1920x1080"
    fhd = "1366x768"
    qhd = "2560x1440"
    uhd = "3840x2160"

def check_resolution(arg):
    "TODO: Check if resolution is from Resolution list"
    pass

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

    global UNSPLASH_URL
    UNSPLASH_URL = cfg.get("photoley", "url")

    def get_url():
        url = f"{UNSPLASH_URL}"
        if _r:=args.resolution:
            check_resolution(_r)
            url += f"/{_r}"

        if _u:=args.user:
            url += f"/user/{_u.lower()}"
        
        if _c:=args.collection:
            url += f"/collection/{_c}"
        
        if _q:=args.query:
            url += f"?{_q.lower()}"

        return url
    
    print(get_url())

if __name__ == "__main__":
    main()
