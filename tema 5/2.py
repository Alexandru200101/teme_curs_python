             # Varianta 1
for n in range(2,1001):
    este_prim = True

    if n < 2:
        este_prim = False
    else:
        for i in range(2, n):
            if n % i == 0:
                este_prim = False
                break

    if este_prim:
        print(f"{n} este număr prim")

    else:
        print(f"{n} NU este număr prim")



           #Varianta 2
# n = int(input("Scrie un număr: "))
# este_prim = True

# if n < 2:
#     este_prim = False
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             este_prim = False
#             break

# if este_prim:
#     print(f"{n} este număr prim (divizibil doar cu 1 și {n})")
# else:
#     print(f"{n} NU este număr prim")