words = ['frig', 'frumos', 'frate']  # poți schimba lista cu orice vrei

# verificăm dacă lista este goală
if len(words) == 0:
    print("Prefix comun: ")
else:
    # presupunem că prefixul comun este primul cuvânt
    prefix = words[0]

    # luăm fiecare cuvânt începând cu al doilea
    for k in range(1, len(words)):
        word = words[k]
        i = 0
        # comparăm caracter cu caracter
        while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
            i += 1
        # reducem prefixul la partea comună
        prefix = prefix[:i]
        # dacă nu mai există prefix comun, ieșim din buclă
        if prefix == "":
            break

    print("Prefix comun:", prefix)
