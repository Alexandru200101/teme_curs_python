from collections import Counter  #Varianta 1 

text1 = input("Scrie primul text: ")
text2 = input("Scrie al doilea text: ")

counter1 = Counter(text1)
counter2 = Counter(text2)

# Intersecția minimă a frecvențelor
litere_comune = counter1 & counter2
print(litere_comune)
  
  #Varianta 2
# text1 = input("Scrie primul text: ")
# text2 = input("Scrie al doilea text: ")

# litere_comune = []

# for litera in text1:
#     if litera in text2 and litera not in litere_comune:
#         litere_comune.append(litera)

# print("Litere comune:", litere_comune)

# Varianta 3
# text1 = input("Scrie primul text: ")
# text2 = input("Scrie al doilea text: ")

# print("Litere comune unice:")

# for i, litera in enumerate(text1):
#     # Verificăm dacă litera există în text2
#     if litera in text2:
#         # Verificăm dacă litera a mai apărut înainte în text1 (ca să evităm duplicate)
#         gasit_inainte = False
#         for j, litera_anterioara in enumerate(text1):
#             if j < i and litera_anterioara == litera:
#                 gasit_inainte = True
#                 break
        
#         if not gasit_inainte:
#             print(litera)
         



    
