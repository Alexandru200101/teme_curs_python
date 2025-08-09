def scor_cuvant(cuvant):
    total = 0
    for litera in cuvant.lower():
        if litera.isalpha():
            total += ord(litera) - ord('a') + 1
    return total

def cuvant_cu_scor_maxim(lista_cuvinte):
    max_cuvant = None
    max_scor = -1

    for cuvant in lista_cuvinte:
        scor = scor_cuvant(cuvant)
        if scor > max_scor:
            max_scor = scor
            max_cuvant = cuvant

    return max_cuvant

cuvinte = ["mama", "ana", "abc", "zz"]
print(cuvant_cu_scor_maxim(cuvinte))  # mama
