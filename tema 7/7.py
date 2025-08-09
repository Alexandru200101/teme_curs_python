files = ['mare_2023.jpeg', 'test.txt', 'liste.py', 'cv.pdf']
paths = {
    'C://Downloads//Images': ['jpg', 'png', 'jpeg'],
    'C://Downloads//Text': ['txt'],
    'C://Downloads//Python_files': ['py'],
    'C://Downloads//PDF': ['pdf'],
}

for i in files:
    found = False
    for path, extensions in paths.items():
        if i.split('.')[-1] in extensions:
            print(i)
            print(f'File {i} should be moved to {path}')
            found = True
            break
    if not found:
        print(f'File {i} has no matching path')