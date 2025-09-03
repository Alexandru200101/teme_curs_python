def caractere_generator(sir):
    for c in sir:
        yield c  
        
sir = "Salut"
gen = caractere_generator(sir)

for c in gen:
    print(c)