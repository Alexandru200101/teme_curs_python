#Varianta 1

# vocale = "aeiou"
# consoane = "bcdfghjklmnpqrstvwxyz"
# text = input("Scrie un text: ")
# count_vocale = 0
# count_consoane = 0
# for i in text:
#     if i.lower() in vocale:
#         count_vocale += 1
# for j in text:
#     if j.lower() in consoane:
#         count_consoane += 1
    
# print(f"Numărul de vocale din text este: {count_vocale}")
# print(f"Numărul de consoane din text este: {count_consoane}")

#Varianta 2 #comprehension
n = input("Scrie un text: ")
vocale = "aeiou"
consoane = "bcdfghjklmnpqrstvwxyz"

count_vocale = sum(1 for i in n if i.lower() in vocale)
count_consoane = sum(1 for j in n if j.lower() in consoane)

print(f"Numărul de vocale din text este: {count_vocale}")
print(f"Numărul de consoane din text este: {count_consoane}")
