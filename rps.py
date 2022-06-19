# Rock, Paper, Scissors by rene.jock@outlook.de

import random, sys, time, os

game_elements = ['Rock','Paper','Scissors']
print('Wellcom to Rock, Paper, Scissors')
player = input('(R)ock,(P)aper or (S)cissor? : ').lower()
ki = random.choice(game_elements)

def player_logic(playerIn):
    if playerIn == 'r':
        print(game_elements[0])
    elif playerIn == 'p':
        print(game_elements[1])
    elif playerIn == 's':
        print(game_elements[2])
    else:
        print('Invalid Input! Please type r,p or s!')

def com_logic(com, game):
    if com == 'Rock':
        print(com)
    elif com == 'Paper':
        print(com)
    elif com == 'Scissors':
        print(com)

def game(com, pl):
    if pl == 'r' and com == 'Rock':
        print('Draw')
    elif pl == 'r' and com == 'Paper':
        print('Com Wins')
    elif pl == 'r' and com == 'Scissors':
        print('Player Wins')
    if pl == 'p' and com == 'Rock':
        print('Player wins')
    elif pl == 'p' and com == 'Paper':
        print('Draw')
    elif pl == 'p' and com == 'Scissors':
        print('Com Wins')
    if pl == 's' and com == 'Rock':
        print('Com wins')
    elif pl == 's' and com == 'Paper':
        print('Player wins')
    elif pl == 's' and com == 'Scissors':
        print('Draw')

def show_menu():
    print('Wellcom to Rock, Paper, Scissors')
    print('')
    print('Titlemenu')
    print('[1] - New Game')
    print('[2] - Exit')
    menu = input('Please select [1] or [2] : ')


if __name__=="__main__":
    #show_menu()
    player_logic(player)
    time.sleep(3)
    com_logic(ki,game_elements)
    game(ki, player)