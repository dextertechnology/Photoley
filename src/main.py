import argparse, string
from enum import Enum

parser = argparse.ArgumentParser(
    prog='getimg',
    usage='%(prog)s [options]',
    description="Using unsplash, fetch random wallpaper with specific size and category.",
    epilog='Enjoy the Photoley')

parser.add_argument('-q', '--query', metavar='', type=str, help="Comma-separated string search query to get relevant random image")
parser.add_argument('-r', '--resolution', metavar='', type=str, help="Resolution of screen. eg: 1920x1080, 1366x768")
parser.add_argument('-u', '--user', metavar='', type=str, help="Username that exists in unsplash eg: erondu")
parser.add_argument('-c', '--collection', metavar='', type=int, help="Integer: Collection that exists in unsplash eg: 190727")

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

if __name__ == "__main__":
    args = parser.parse_args()
    print(get_url())