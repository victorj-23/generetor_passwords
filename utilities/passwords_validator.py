import re


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
