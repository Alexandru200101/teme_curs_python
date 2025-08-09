def count_smaller_numbers(nbs):
    rezultat = []
    for x in nbs:
        count = 0
        for y in nbs:
            if y < x:
                count += 1
        rezultat.append(count)
    return rezultat

# Test:
nbs = [3, 7, 8, 5]
print(count_smaller_numbers(nbs))  # Output: [0, 2, 3, 1]
