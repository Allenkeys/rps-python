import random

comp = ['R', 'P', 'S']

def comp_choice():
    return random.choice(comp)


def player_choice():
    isValid = False
      
    while isValid == False:
        choice = input('R: Rock\nP: Paper\nS: Scissors\nSelect option\n>>>').upper().strip()

        if choice in comp:
            isValid = True
            return choice
        else:
            print('>>>Invalid selection, try again...')
    return choice        
 
# def check_choice():

def game():
    computer = comp_choice()
    player = player_choice()
    print(f'Player({player}): CPU({computer})')

    if player == computer:
        print('It\'s a tie')
        print('*'*12)
        game()
    elif ((player == 'R' and computer == 'S') or 
        (player == 'S' and computer =='P') or 
        (player == 'P' and computer == 'R')):

        print('*'*12)
        print('Player won!')
    else:
        print('*'*12)
        print('Computer won!')    



game()   