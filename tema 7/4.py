employee = {
    1: {'name': 'Andrei', 'salary': 100},
    2: {'name': 'Vlad', 'salary': 500},
    3: {'name': 'Ioana', 'salary': 330}
}
# Varianta 1 : modiicam salariile tuturor angajaților
# for i in employee:
#     print(f"Angajat: {employee[i]['name']}")
#     print(f"  Salariul inițial: {employee[i]['salary']}")
#     nou_salariu = int(input(f"  Introdu noul salariu pentru {employee[i]['name']}: "))
#     employee[i]['salary'] = nou_salariu
#     print(f"  Salariul actualizat: {employee[i]['salary']}")
#     print("-" * 40)  # linie separator
    
# print("\n*** Salariile actualizate pentru toți angajații ***")
# for i in employee:
#     print(f"{employee[i]['name']}: {employee[i]['salary']}")


# Varianta 2 : modificăm salariul unui angajat specificat de utilizator

alegere_id = int(input("Introdu ID-ul angajatului căruia vrei să îi schimbi salariul: "))

if alegere_id not in employee:
    print(f"Angajatul cu ID {alegere_id} nu există.")
else:
    angajat = employee[alegere_id]
    print(f"Ai ales angajatul {angajat['name']} cu salariul actual: {angajat['salary']}")
    nou_salariu = int(input(f"Introdu noul salariu pentru {angajat['name']}: "))
    employee[alegere_id]['salary'] = nou_salariu
    print(f"Salariul pentru {angajat['name']} a fost actualizat la {nou_salariu}.")
print(employee)
print("\n*** Salariile actualizate pentru toți angajații ***")




# Solicităm ID-ul angajatului
# alegere_id = int(input("🔎 Introdu ID-ul angajatului căruia vrei să îi modifici salariul: "))

# # Verificăm dacă ID-ul există
# angajat = employee.get(alegere_id)

# if angajat is None:
#     print(f"⚠️ Angajatul cu ID-ul {alegere_id} nu există.")
# else:
#     print(f"\n👤 Angajat selectat: {angajat['name']}")
#     print(f"💰 Salariu curent: {angajat['salary']}")

#     # Solicităm noul salariu
#     try:
#         nou_salariu = int(input(f"✏️ Introdu noul salariu pentru {angajat['name']}: "))
#         angajat['salary'] = nou_salariu
#         print(f"\n✅ Salariul actualizat pentru {angajat['name']}: {nou_salariu}")
#     except ValueError:
#         print("⚠️ Valoare invalidă introdusă. Salariul trebuie să fie un număr întreg.")

        
