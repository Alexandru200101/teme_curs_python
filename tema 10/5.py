def are_caractere_unice(cuvant):
    return len(set(cuvant)) == len(cuvant)
print(are_caractere_unice("abcde"))    # True
print(are_caractere_unice("abca"))     # False
print(are_caractere_unice("12345"))    # True
print(are_caractere_unice("112345"))   # False
