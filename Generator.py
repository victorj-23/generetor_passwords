import random

drawing_asc2 =''' 
  _____                                    _        _____                           _             
 |  __ \                                  | |      / ____|                         | |            
 | |__) |_ _ ___ _____      _____  _ __ __| |___  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` / __| | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |  | (_| \__ \__ \\ V  V / (_) | | | (_| \__ \ | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|___/  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|                                                                                                  
'''
print('\033[32m' + drawing_asc2 + '\033[0;0m')

passwords = int(input('How many passwords do you want? '))
lenght = int(input('What length for the passwords? '))

chars = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
special_chars = '.+-[]*~_@#:?'

for _ in range(passwords):
    generate_passwords = ''
    for _ in range(lenght - 1):
        generate_passwords += random.choice(chars)
    generate_passwords += random.choice(special_chars)
    print(generate_passwords)
