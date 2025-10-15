import numpy as np

def f(array):
    return np.where(array > 25)[0].tolist()

if __name__ == "__main__":
    array = np.arange(0, 51)
    print(f(array))