text = input("Introduceti un text: ") #Varianta 1
spatii_goale = 0

litere_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
litere_count = 0

numere_string = "0123456789"
numere_count = 0

caractere_speciale_string = "!@#$"
caractere_speciale_count = 0

for i in text:
    if i == " ":
        spatii_goale += 1

    if i in litere_string:
        litere_count += 1

    if i in numere_string:
        numere_count += 1

    if i in caractere_speciale_string:
        caractere_speciale_count += 1

print(f"Lungimea textului este: {len(text)}")
print("Număr spații goale:", spatii_goale)
print("Număr litere:", litere_count)
print("Număr cifre:", numere_count)
print("Număr caractere speciale:", caractere_speciale_count)

# Varianta 2
# def numara_caractere(text):
#     litere = 0
#     cifre = 0
#     spatii = 0
#     simboluri = 0

#     for caracter in text:
#         if caracter.isalpha():
#             litere += 1
#         elif caracter.isdigit():
#             cifre += 1
#         elif caracter.isspace():
#             spatii += 1
#         else:
#             simboluri += 1

#     return litere, cifre, spatii, simboluri

# def afiseaza_rezultat(text):
#     litere, cifre, spatii, simboluri = numara_caractere(text)
#     print(f"Lungimea textului este: {len(text)}")
#     print(f"Număr litere: {litere}")
#     print(f"Număr cifre: {cifre}")
#     print(f"Număr spații: {spatii}")
#     print(f"Număr simboluri: {simboluri}")

# # Program principal
# text = input("Introduceti un text: ")
# afiseaza_rezultat(text)