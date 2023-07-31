import random


def give_char():
    chars = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return random.choice(chars)

def give_special_char():
    special_chars = '.+-[]*~_@#:?'
    return random.choice(special_chars)
