import os
import subprocess


VERSION = "1.0.1"

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

_MEDIA_DIR = '/tmp/photoley'

if not os.path.exists(_MEDIA_DIR):
    print("Creating media directory")
    os.mkdir(_MEDIA_DIR)

MEDIA_DIR = _MEDIA_DIR

_CONFIG_DIR = '/etc/photoley'


if not os.path.exists(_CONFIG_DIR):
    user = os.geteuid()
    group = os.getegid()
    p = subprocess.Popen(
        [f"sudo mkdir {_CONFIG_DIR} && sudo chown -R {user}:{group} {_CONFIG_DIR}"],
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
        shell=True
    )

    (out, err) = p.communicate()

    if err:
        print(err)

CONFIG_DIR = _CONFIG_DIR

UNSPLASH_URL = 'https://source.unsplash.com'
