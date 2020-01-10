import os

from photoley.utilities.json_parser import JSONParser
from photoley.photoley import config


class Configure:
    def __init__(self, args):
        self.args = args
    
    def configure(self):
        config_file = os.path.join(config.CONFIG_DIR, 'photoley.json')

        context = {}
        for arg in vars(self.args):
            context[arg] = getattr(self.args, arg)

        conf = JSONParser(config_file)
        conf.insert(context=context)
