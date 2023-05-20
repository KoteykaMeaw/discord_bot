import random


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


def gen_emodji():
    emodji = [":)", ":(", ":0", "._."]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 3)
    if flip == 0:
        return "ОРЕЛ"
    if flip == 1:
        return "ОРЕЛ"
    else:
        return "РЕШКА"

def gameee():
    gamee = random.randint(0, 2)
    if gamee == 0:
        return "Роблокс"
    if gamee == 1:
        return "Майнкрафт"
    else:
        return "Что нибудь другое"


