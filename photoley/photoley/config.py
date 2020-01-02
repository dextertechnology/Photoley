import os


VERSION = "1.0.1"

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

_MEDIA_DIR = '/tmp/photoley'

if not os.path.exists(_MEDIA_DIR):
    print("Creating directory")
    os.mkdir(_MEDIA_DIR)

MEDIA_DIR = _MEDIA_DIR

UNSPLASH_URL = 'https://source.unsplash.com'
