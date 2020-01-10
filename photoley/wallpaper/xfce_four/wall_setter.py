import os
import subprocess

from photoley.photoley.config import MEDIA_DIR, CONFIG_DIR
from photoley.utilities.json_parser import JSONReader


def set_wallpaper(img, **kwargs):
    """
        XFCE-4
        =======
        Introduction
        ------------
        In xfce4 based desktop environment, xfconf-query is
        a commandline utility which is here used for setting
        desktop wallpaper.

        Check Property
        --------------
        To check property, `xfconf-query -c <channel_name> -m`
        Here, -m is used for monitoring. Try to change desktop
        wallpaper of the workspace you prefer, then you will get
        screen propery like:
        `/backdrop/screen0/monitorDP1/workspace0/last-image`
        Use that as a property.
    """

    data = JSONReader(os.path.join(CONFIG_DIR, 'photoley.json'))
    # _property = "/backdrop/screen0/monitoreDP-1/workspace2/last-image"
    # _channel = "xfce4-desktop"
    _property = data.read_line('property')
    _channel = data.read_line('channel')

    _img = os.path.abspath(os.path.join(MEDIA_DIR, img))

    if not os.path.isfile(_img):
        raise Exception("File doesn't exist.")

    command = f"xfconf-query --channel {_channel} \
        --property {_property} --set {_img}"
    
    print(f"Set image {_img}")
    try:
        shell_cmd = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (output, err) = shell_cmd.communicate()
        shell_cmd.wait()
        return output
    except Exception as e:
        return e
