def hash_decorator(func):
    def decorate(*args, **kwargs):
        print("#####################################################################")
        func(*args, **kwargs)
        print("#####################################################################")  
    
    return decorate