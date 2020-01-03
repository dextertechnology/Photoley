import os
import subprocess

from photoley.photoley.config import MEDIA_DIR


def set_wallpaper(img, **kwargs):
    _property = "/backdrop/screen0/monitorDP1/workspace0/last-image"
    _channel = "xfce4-desktop"

    _img = os.path.abspath(os.path.join(MEDIA_DIR, img))

    if not os.path.isfile(_img):
        raise Exception("File doesn't exist.")
    
    print(f"Set image {_img}")
    return subprocess.call([
        "xfconf-query",
        "--channel",
        kwargs.get("channel", _channel),
        "--property",
        kwargs.get("property", _property),
        "--set",
        _img
    ], shell=True, universal_newlines=True)
