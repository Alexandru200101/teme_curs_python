def file_type(file_name):
    extensie = file_name.lower().split('.')[-1]  # luăm extensia (cu litere mici)

    tipuri = {
        'jpeg': 'imagine',
        'jpg': 'imagine',
        'png': 'imagine',
        'gif': 'imagine',
        'txt': 'text',
        'md': 'text',
        'doc': 'text',
        'docx': 'text',
        'mp3': 'muzica',
        'wav': 'muzica',
        'flac': 'muzica'
    }

    return tipuri.get(extensie, 'necunoscut')  # dacă extensia nu e cunoscută

# Exemple de test:
print(file_type('20221107.jpeg'))        # imagine
print(file_type('test.txt'))             # text
print(file_type('music_20221107.mp3'))   # muzica
print(file_type('fisier.unknown'))       # necunoscut
