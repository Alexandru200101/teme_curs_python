numbers = [1, 1, 3, 7, 9, 2, 3, 100, 9, 333, 2.0, 5, 1, 3, 3]

# from collections import Counter
# counter = Counter(numbers)
# print(counter)




aparitii = {}  # dicționar gol

for elem in numbers:
    if elem in aparitii:
        aparitii[elem] += 1  # crește contorul
    else:
        aparitii[elem] = 1   # prima apariție

print(aparitii)
print("Numărul de elemente unice:", len(aparitii))

# aparitii = {elem: numbers.count(elem) for elem in set(numbers)}

# print(aparitii)