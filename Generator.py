import random

print('Password Generator')
print('-' * 19)

passwords = int(input('How many passwords do you want? '))
leght = int(input('What length for the passwords? '))

chars = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for _ in range(passwords):
    generate_passwords = ''
    for _ in range(leght):
        generate_passwords += random.choice(chars)
    print(generate_passwords)
