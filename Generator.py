import random
import re

def give_char():
    chars = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return random.choice(chars)

def give_special_char():
    special_chars = '.+-[]*~_@#:?'
    return random.choice(special_chars)

def check_password(string):
    if not re.search(r'\d', string):
        return False
    if not re.search(r'[A-Z]', string):
        return False
    if not re.search(r'[a-z]', string):
        return False
    if not re.search(r'[.,+,-,\[,\],*,~,_,@,#,:,?]', string):
        return False

    return True

drawing_asc2 =''' 
  ___                              _       ___                       _           
 | _ \__ _ _______ __ _____ _ _ __| |___  / __|___ _ _  ___ _ _ __ _| |_ ___ _ _ 
 |  _/ _` (_-<_-< V  V / _ \ '_/ _` (_-< | (_ / -_) ' \/ -_) '_/ _` |  _/ _ \ '_|
 |_| \__,_/__/__/\_/\_/\___/_| \__,_/__/  \___\___|_||_\___|_| \__,_|\__\___/_|  
                                                                                                                                                                                                                                                                                                
'''
print('\033[32m' + drawing_asc2 + '\033[0;0m')

while True:
    try:
        passwords = int(input('How many passwords do you want? '))
        lenght = int(input('What length for the passwords? '))
        if passwords < 1  or lenght < 1:
            print('\033[31m' + 'ERROR: Use positives numbers' + '\033[0;0m')  
            continue
        break
    except ValueError:
        print('\033[31m' + 'ERROR: Use integers numbers' + '\033[0;0m')

list_passwords =[]

while len(list_passwords) < passwords:
    generate_password = ''
    for _ in range(lenght - 1):
        generate_password += give_char()
    generate_password += give_special_char()

    if check_password(generate_password):
        list_passwords.append(generate_password)

for p in list_passwords:
    print(p)
