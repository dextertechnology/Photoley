import string

from enum import Enum


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

class GetUrl:
    def __init__(self, url, args):
        self.url = url
        self.args = args

    def get_url(self):
        url = self.url
        if _r:=self.args.resolution:
            check_resolution(_r)
            url += f"/{_r}"

        if _u:=self.args.user:
            url += f"/user/{_u.lower()}"
        
        if _c:=self.args.collection:
            url += f"/collection/{_c}"
        
        if _q:=self.args.query:
            url += f"?{_q.lower()}"

        if not _u and not _c:
            url = url.replace('.com', '.com/random')

        return url
