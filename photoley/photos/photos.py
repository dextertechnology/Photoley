import uuid
from urllib import request

from .get_url import GetUrl
from photoley.photoley import config
from photoley.utilities.stdout import hash_decorator, PrintProgressBar


class Photos:
    def __init__(self, **kwargs):
        self.url = kwargs.get('url', None)
        self.args = kwargs.get('args', None)
        self.dir = kwargs.get('dir', None)

    @hash_decorator
    def save(self):
        get_url = GetUrl(self.url, self.args).get_url()
        uid = str(uuid.uuid4())

        req = request.urlopen(get_url)

        with open(f"{config.MEDIA_DIR}/{uid}.jpg", 'wb') as fp:
            l = int(req.headers.get('Content-Length'))//1024
            PrintProgressBar(0, l, prefix= 'Progress:', suffix= 'Complete', length= 50)

            new_range = list(range(0, l))
            for i, item in enumerate(new_range):
                chunk = req.read(1024)
                
                if not chunk: break
                fp.write(chunk)
                PrintProgressBar(i + 1, l, prefix= 'Progress:', suffix= 'Complete', length= 50)


        print('\n', get_url)
        print(f"Saved in {str(config.MEDIA_DIR)}")
        return get_url
