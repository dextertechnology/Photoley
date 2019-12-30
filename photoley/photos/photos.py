from photos.get_url import GetUrl
from utilities.stdout import hash_decorator


class Photos:
    def __init__(self, **kwargs):
        self.url = kwargs.get('url', None)
        self.args = kwargs.get('args', None)
        self.dir = kwargs.get('dir', None)

    @hash_decorator
    def save(self):
        get_url = GetUrl(self.url, self.args).get_url()
        
        print(get_url)
        return get_url
