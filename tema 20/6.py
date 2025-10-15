import numpy as np

def f(array):
    minim = np.min(array)
    maxim = np.max(array)
    
    
    min_pos = list(zip(*np.where(array == minim)))
    max_pos = list(zip(*np.where(array == maxim)))

    return f"Matricea generată:\n{array}\n\nValoarea minimă: {minim}\nPoziția valorii minime: {min_pos}\n\nValoarea maximă: {maxim}\nPoziția valorii maxime: {max_pos}"

if __name__ == "__main__":
    array = np.random.randint(0, 21, size=(4,4))
    print(f(array))
