import random

comp = ['R', 'P', 'S']

def comp_choice():
    return random.choice(comp)

def player_choice():
    choice = input('R: Rock\nP: Paper\nS: Scissors\nSelect option\n>>>')
    return choice.upper()

print(player_choice())    