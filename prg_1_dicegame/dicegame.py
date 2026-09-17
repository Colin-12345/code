import random
import time
x = 0
y = 0
player1score= 0
player2score= 0
win=False
active = False
keep_rolling= True

print ('hello, welcome to dice game')
time.sleep(1)
x=int(input('please press 1 to begin '))
if x == 1:
    active=True

if active == True:
    while keep_rolling == True:
        if int(input('player 1, click 5 to roll dice ')) == 5:
            player1score += int(random.randint(1, 6))
            if player1score < 21:
                if y:=input(f'your score is {player1score}! keep rolling? ') == 'yes':
                    keep_rolling = True
                elif y == 'no':
                    keep_rolling = False
                else:
                    print ('im taking that as a no!')
                    keep_rolling = False
            elif player1score == 21:
                print ('player1 wins!')
                active=False
                break
            elif player1score > 21:
                print ('player2 wins! bust!')
                active = False
                break
    keep_rolling = True
    if active == True:
        while keep_rolling == True:
            if int(input('player 2, click 5 to roll dice ')) == 5:
                player2score += int(random.randint(1, 6))
                if player2score < 21:
                    if y:=input(f'your score is {player2score}! keep rolling? ') == 'yes':
                        keep_rolling = True
                    elif y == 'no':
                        keep_rolling = False
                    else:
                        print ('im taking that as a no!')
                        keep_rolling = False
                elif player2score == 21:
                    print ('player2 wins!')
                    active = False
                    break 
                elif player2score > 21: 
                    print ('player1 wins! bust!')
                    active=False
                    break
        if active == True:
            print ('calculating winner')
            for i in range (0, 3):
                print ('.')
                time.sleep (1)
            if player1score>player2score:
                print('player1 wins!')
            elif player2score>player1score:
                print('player2 wins!')
            else:
                print('its a tie!')
    time.sleep(1)
    print (f'player1score = {player1score}')
    time.sleep(1)
    print (f'player2score = {player2score}')
    time.sleep(1)
    print ('game end')

    



