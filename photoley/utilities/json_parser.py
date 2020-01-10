import os
import json


class _JSONFile:
    def __init__(self, file):
        self.file = file
    
    def open(self):
        try:
            with open(self.file, mode='r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError as e:
            print("Creating file...")
            os.mknod(self.file)
            return {}
        except json.decoder.JSONDecodeError as e:
            print("No key exists")
            return {}
        except Exception as e:
            return e

class JSONParser(_JSONFile):
    def insert(self, context=None):
        if not context:
            return None
        
        file = self.open()

        for k, v in context.items():
            file[k] = v
 
        with open(self.file, mode='w') as f:
            json.dump(file, f, indent=4)
        
        print("Item/s inserted")
        return context

    def delete(self, context=None):
        if not context:
            return None

        file = self.open()
        
        for k, v in context.items():
            try:
                del file[k]
            except KeyError:
                print("Key doesn't exists")
                return {k: v}

        with open(self.file, mode='w') as f:
            json.dump(file, f, indent=4)
        
        print("Item/s deleted")
        return context

class JSONReader(_JSONFile):
    def read_all(self):
        return self.open()

    def read_line(self, key):
        try:
            file = self.open()
            return file[str(key)]
        except KeyError as e:
            print("Key does not exists")
            return
