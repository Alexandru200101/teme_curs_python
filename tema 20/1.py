import numpy as np

def vector(array):
    return array[array % 2 == 0]

if __name__ == "__main__":
    array = np.array([0,1,2, 3, 4, 5, 6,7,8,9])
    print(vector(array))