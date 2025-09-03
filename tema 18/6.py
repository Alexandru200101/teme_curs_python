def triple_call(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            func(*args, **kwargs)  
    return wrapper


@triple_call
def salut():
    print("Salut lume!")

salut()
