# Rock, Paper, Scissors by rene.jock@outlook.de

import random, sys, time, os

#TODO initialize game elements to selection.
game_elements = ['Rock', 'Paper' , 'Scissors']
player_score = 0
cpu_score = 0
player = input('Choose (R)ock, (P)aper or (S)scissors: ').lower()
cpu = random.choice(game_elements)

def game_logic(pl, com, plPoints, cpuPoints):
    if pl == 'Rock' and com == "Scissors":
        plPoints += 1
        print(cpu)
        print('Player wins! Player- Score: ', plPoints )

    elif pl == 'Rock' and com == 'Paper':
        cpuPoints += 1
        print(cpu)
        print('Computer wins! Comuter- Score: ', cpuPoints )

    elif pl == 'Rock' and com == 'Rock':
        print(cpu)
        print('Draw')

    elif pl == 'Paper' and com == 'Scissors':
        cpuPoints += 1
        print(cpu)
        print('Computer wins! Comuter- Score: ', cpuPoints )

    elif pl == 'Paper' and com == 'Paper':
        print(cpu)
        print('Draw')

    elif pl == 'Paper' and com == 'Rock':
        plPoints += 1
        print(cpu)
        print('Player wins! Player- Score: ', plPoints )

    else:
        print('Invalid Input!')
   

game_logic(player, cpu, player_score, cpu_score)