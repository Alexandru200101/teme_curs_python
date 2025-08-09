def suma_cifre(s):
    return sum(int(c) for c in s if c.isdigit())


s = 'eu am 33 de ani'
print(suma_cifre(s))  # 3 + 3 = 6
