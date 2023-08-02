def save_password(pre_list):
    while True:
        question = str(input('Do you want to save in .txt [Yes/No] ? ')).upper()
        if question[0] != 'Y' and question[0] != 'N':
            print('\033[31m' + 'ERROR: Use Yes or No in the answer!' + '\033[0;0m')
            continue
        else:
            break    
    
    if question[0] == 'Y':
        existing_passwords = []
    try:
        with open('passwords.txt', 'r') as archive:
            existing_passwords = archive.read().splitlines()
    except FileNotFoundError:
        pass

    updated_passwords = existing_passwords + pre_list

    with open('passwords.txt', 'w') as exit:
        for passwords in updated_passwords:
            print(passwords, file=exit)
        exit.write('-' * len(max(pre_list, key=len)))