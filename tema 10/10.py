def triunghi(n):
    for i in range(n):
        # numarul de '*' pe randul i este 2*i + 1
        print('*' * (2 * i + 1))

# Exemplu:
n = int(input("Introdu n: "))
triunghi(n)
