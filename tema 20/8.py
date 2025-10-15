import numpy as np

def f(array):
    r = array.reshape((3,4))
    t = r.T
    return f"Matricea inițială:\n{array}\n\nMatricea reshaped (3x4):\n{r}\n\nMatricea transpusă (4x3):\n{t}"


if __name__ == "__main__":
    array = np.arange(1,13)
    print(f(array))
