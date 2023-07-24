def give_char():
    import random
    chars = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return random.choice(chars)

def give_special_char():
    import random
    special_chars = '.+-[]*~_@#:?'
    return random.choice(special_chars)

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
        break
    except ValueError:
        print('\033[31m' + 'ERROR: Use integers numbers' + '\033[0;0m')

for _ in range(passwords):
    generate_passwords = ''
    for _ in range(lenght - 1):
        generate_passwords += give_char()
    generate_passwords += give_special_char()
    print(generate_passwords)
