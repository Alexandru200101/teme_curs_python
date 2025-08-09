list1 = [7, 2, 9, [2, 30], "Catalin", 5, 10.12, None]
list2 = []

list2 = [i for i in list1 if type(i) == int or type(i) == float]
    
print(list2)

if len(list2) == 0:
    print("nu exista numere")
else:
    print(max(list2))
