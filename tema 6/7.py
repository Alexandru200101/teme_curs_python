# Varianta 1
words = ['python', 'ruby', 'javascript']
new_words = []

for word in words:
    invers = word[::-1]       # inversăm fiecare cuvânt
    new_words.append(invers)  # adăugăm în lista nouă

print(new_words)


# Varianta 2 (list comprehension)

# words = ['python', 'ruby', 'javascript']
# new_words = [word[::-1] for word in words]
# print(new_words)

# Varianta 3 (funcție)

# def inversare_cuvinte(words):
#     return [word[::-1] for word in words]


# # exemplu de utilizare
# words = ['python', 'ruby', 'javascript']   
# new_words = inversare_cuvinte(words)
# print(new_words)

