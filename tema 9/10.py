cars = {
    'Dacia': 15000,
    'Toyota': 20000,
    'BMW': 50000,
    'Audi': 45000,
    'Hyundai': 16500,
    'Mercedes': 70000
}

euro = {k:v*5 for k,v in cars.items()}
print(euro)

dictionar2 = {masina:brand for masina,brand in cars.items() if brand > 20000}
print(dictionar2)