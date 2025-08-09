def safe_divide(a, b):
    try:
        # Verificăm dacă a și b sunt de tip numeric (int sau float)
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Valori invalide")
        if b == 0:
            return "Impartire la zero interzisa!"
    except TypeError:
        return "Valori invalide"
    else:
        return a / b


print(safe_divide(10, 2))      # 5.0
print(safe_divide(10, 0))      # Impartire la zero interzisa!
print(safe_divide(10, "a"))    # Valori invalide
print(safe_divide("a", 2))     # Valori invalide
