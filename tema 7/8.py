cars = {
    'Dacia': 15000,
    'Toyota': 20000,
    'BMW': 50000,
    'Audi': 45000,
    'Hyundai': 16500,
    'Mercedes': 70000
}
# dictionar_filtrat = {}


# for cheie, valoare in cars.items():
#     if valoare > 40000:
#         dictionar_filtrat[cheie] = valoare

# print(dictionar_filtrat)

dictionar = {cheie: valoare for cheie, valoare in cars.items() if valoare > 40000}
print(dictionar)

# for key,value in cars.items():
#     value = value * 5  
#     cars[key] = value
# print(cars)

# # cars = {key: value * 5 for key, value in cars.items()}
# # print(cars)