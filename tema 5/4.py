# username = "Press 1 to see the username"    #Varianta 1
# password = "Press 2 to see the password"
# email = "Press 3 to see the email"
# show_details = "Press 4 to see all details"

# while True:
#     user_input = input("Apasa 1 pentru a vedea numele de utilizator, 2 pentru parola, 3 pentru email, 4 pentru toate detaliile sau 'q' pentru a iesi: ")

#     if user_input == '1':
#         print(username)
#     elif user_input == '2':
#         print(password)
#     elif user_input == '3':
#         print(email)
#     elif user_input == '4':
#         print(show_details)
        
#     elif user_input == 'q':
#         break
#     else:
#         print("Optiune invalida. Te rog incearca din nou.")


# username = input("Enter your username: ")            #Varianta 2
# password = input("Enter your password: ")
# email = input("Enter your email: ")
# show_details = f"Username: {username}, Password: {password}, Email: {email}"


# while True:
#     user_input = input("Press 1 to see the username, 2 for the password, 3 for the email, 4 for all details or 'q' to quit: ")

#     if user_input == '1':
#         print(username)
#     elif user_input == '2':
#         print(password)
#     elif user_input == '3':
#         print(email)
#     elif user_input == '4':
#         print(show_details)
#     elif user_input.lower() == 'q':
#         break
#     else:
#         print("Invalid option. Please try again.")




# Varianta 3
username_real = "Alex" #datele acestea se pot salva intr-o bază de date
password_real = "Parola123"
email_real = "alex@example.com"
show_details_real = f"Username: {username_real}, Password: {password_real}, Email: {email_real}"

incercari = 0
max_incercari = 3

while incercari < max_incercari:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    email = input("Enter your email: ")

    if username == username_real and password == password_real and email == email_real:
        print("Login successful!")
        break
    else:
        incercari += 1
        print(f"Login failed. Please try again. Ai încercat de {incercari} ori.")

if incercari == max_incercari:
    print("Ai depășit numărul maxim de încercări. Acces blocat.")
else:
    # Dacă loginul a reușit, intră aici:
    while True:
        user_input = input("Press 1 to see the username, 2 for the password, 3 for the email, 4 for all details or 'q' to quit: ")

        if user_input == '1':
            print(username_real)
        elif user_input == '2':
            print(password_real)
        elif user_input == '3':
            print(email_real)
        elif user_input == '4':
            print(show_details_real)
        elif user_input.lower() == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")