def only_int_args(func):
    def wrapper(*args, **kwargs):
        if all(isinstance(arg, int) for arg in args) and all(isinstance(v, int) for v in kwargs.values()):
            return func(*args, **kwargs)  
        else:
            print("Eroare: Toate argumentele trebuie să fie int!")
            return None  
    return wrapper

@only_int_args
def adunare(a, b):
    return a + b

print(adunare(3, 4))   
print(adunare(3, "4")) 
