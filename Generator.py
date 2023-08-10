from utilities import *

facade()

# Data entry and some checks take place
while True:
    try:
        amount_passwords = int(input('How many passwords do you want? '))
        lenght = int(input('''What lenght for the passwords \033[31m(Min = 4)\033[0;0m? '''))
        if amount_passwords < 1  or lenght < 1:
            print(red_txt('ERROR: Use positives numbers'))
            continue
        if lenght < 4:
            print(red_txt('ERROR: lenght below 4 is not accepted'))
            continue
        if lenght < 8:
            print(green_txt('Tip: use passwords with at least 8 characters'))
        break
    except ValueError:
        print(red_txt('ERROR: Use integers numbers'))

list_passwords =[]

# Generator working
while len(list_passwords) < amount_passwords:
    genereted_password = ''
    for _ in range(lenght - 1):
        genereted_password += give_char()
    genereted_password += give_special_char()

    # The password needs to meet some requirements
    if check_password(genereted_password): 
        list_passwords.append(genereted_password)

for passwords in list_passwords:
    print(passwords)

save_password(list_passwords)
