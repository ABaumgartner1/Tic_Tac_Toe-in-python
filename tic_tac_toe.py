# Text-based tic tac toe game created in Python by Aaron Baumgartner in 2021
# This game involves some text-based UI

import random

def display_board(played):
    print(" {} | {} | {} \n-----------\n {} | {} | {} \n-----------\n {} | {} | {} ".format(played[1],played[2],played[3],played[4],played[5],played[6],played[7],played[8],played[9]))

def player_input():
    marker = ''
    while(marker.lower() != 'x' and marker.lower() != 'o'):
        marker = input("Would you like x's or o's? ")
    if marker.lower() == 'x':
        return 'x','o'
    else:
        return 'o','x'

def place_marker(played, marker, position):
    played[position] = marker

def win_check(played):
    for i in range(1,len(played)+1,3):
        if ((played[i] == played[i+1] == played[i+2]) and (played[i]=='x' or played[i]=='o')):
            return True
    if ((played[1] == played[4] == played[7]) and (played[1]=='x' or played[1]=='o')):
        return True
    elif ((played[2] == played[5] == played[8]) and (played[2]=='x' or played[2]=='o')):   
        return True 
    elif ((played[3] == played[6] == played[9]) and (played[3]=='x' or played[3]=='o')):
        return True
    elif ((played[1] == played[5] == played[9]) and (played[1]=='x' or played[1]=='o')):
        return True
    elif ((played[3] == played[5] == played[7]) and (played[3]=='x' or played[3]=='o')):
        return True
    return False

def choose_first():
    value = random.randint(0,1)
    if value == 1:
        return "player 1"
    else:
        return "player 2"

def space_check(space,played):
    if played[space] == ' ':
        return True
    return False

def full_board(played):
    for i in played:
        if played[i]==' ':
            return False
    return True

def player_choice(played, marker):
    position = int(input("Where would you like to play? "))
    while(space_check(position,played) == False):
        position = int(input("That space is already taken, please select a new space "))
    place_marker(played, marker, position)

def replay():
    again = input('Would you like to play again(y/n)? ')
    if again.lower() == 'y':
        return True
    return False

print('Welcome to Tic Tac Toe!')

while True:
    p1Marker,p2Marker = player_input()
    played = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
    display_board(played)
    order = choose_first()
    
    while True:
        if order == "player 1":
            print("Player 1, ")
            player_choice(played, p1Marker)
            print('\n'*100)
            display_board(played)
            if win_check(played):
                print("Player 1 wins!\n")
                break
            if full_board(played):
                break
            print("Player 2, ")
            player_choice(played, p2Marker)
            if win_check(played):
                print("Player 2 wins!\n")
                break
            if full_board(played):
                break
            print('\n'*100)
            display_board(played)
        if order == "player 2":
            print("Player 2, ")
            player_choice(played, p2Marker)
            print('\n'*100)
            display_board(played)
            if win_check(played):
                print("Player 2 wins!")
                break
            if full_board(played):
                break
            print("Player 1, ")
            player_choice(played, p1Marker)
            if win_check(played):
                print("Player 2 wins!")
                break
            if full_board(played):
                break
            print('\n'*100)
            display_board(played)
            
    if not replay():
        break