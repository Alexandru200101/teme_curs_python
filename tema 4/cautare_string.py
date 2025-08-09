#Varianta 1

# command = "platform: Solaris; version: 2.5; username: mcristi; rights: all rights reserved"


# for item in command.split(";"):
#     if item.strip().startswith("username:"):
#         username = item.split(":", 1)[1].strip()
#         print(username)  # afișează 'mcristi'
#         break

#Varianta 2
command = "platform: Solaris; version: 2.5; username: mcristi; all rights reserved to …"
result = {}
for item in command.split("; "):
    
    if ":" in item:
        key, value = item.split(":", 1)
        result[key.strip()] = value.strip()
    else:
        print(f"Element fără cheie-valoare: '{item}'")

if value := result.get("username"):
    print(f"Username găsit: {value}")
    

