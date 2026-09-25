import random
import time
x = 0
y = 0
player1score= 0
player2score= 0
win=False
active = False
keep_rolling= True
Bot_play=False
Bot = 'none'

print ('hello, welcome to dice game')
time.sleep(1)
for i in range (0, 100000000000000):
    x=int(input('please press 1 to begin, press 2 to toggle bot play.'))
    if x == 2:
        if Bot_play == False:
            print('bot play is now active')
            Bot_play = True
        elif Bot_play == True:
            print('bot play is no longer active')
            Bot_play = False
    if x == 1:
        active=True
        break
while Bot_play == True:
    time.sleep (1)
    print('gambler 1')
    print('easy 2')
    print('medium 3')
    print('expert 4')
    print('The House 5')
    print('information 6')
    time.sleep (1)
    x = int(input('please select a bot to play against'))
    if x == 1:
        print('gambler selected.')
        Bot='gambler'
        break
    elif x == 2:
        print('easy selected')
        Bot='easy'
        break
    elif x == 3:
        print ('medium selected')
        Bot='medium'
        break
    elif x == 4:
        print ('expert selected')
        Bot='expert'
        break
    elif x == 5:
        print ('The House selected')
        Bot='Rigged'
        for i in range (0, 3):
            time.sleep (1)
            print ('...')
        time.sleep(1)
        print ('good luck.')
        break
    elif x == 6:
        print ('gambler: Never stops rolling, 21 or bust.')
        print ('easy: just here for fun, has a 50% chance to stop rolling.')
        print ('medium: getting serious, will take into account your score but not its current score.')
        print ('expert: plays perfectly')
        print ('The house: rigged against you, able to go up to 23 meaning 21 isnt an instant win.')


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
                if Bot == 'Rigged':
                    print('your chances are good.')
                    keep_rolling = False
                else:
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
            if Bot_play == True:
                if Bot == 'gambler':
                    time.sleep (1)
                    print ('lets go gambling')
                    while Bot == 'gambler':
                        player2score += random.randint(1, 6)
                        time.sleep (1)
                        print(f'Player2score: {player2score}')
                        if player2score < 21:
                            time.sleep (1)
                            print('Let it ride.')
                            keep_rolling = True
                        elif player2score == 21:
                            time.sleep (1)
                            print('JACKPOOOOOOOOOOOOOOOOOOOOOT')
                            keep_rolling = False
                            active = False
                            break
                        elif player2score > 21:
                            time.sleep (1)
                            print('the house always has the edge roy, the house is edging.')
                            keep_rolling = False
                            active = False
                            break
                elif Bot == 'easy':
                    time.sleep (1)
                    print ('Lets just have fun!')
                    while Bot == 'easy':
                        player2score += random.randint(1, 6)
                        time.sleep (1)
                        print(f'Player2score: {player2score}')
                        time.sleep (1)
                        if player2score < 21:
                            x = random.randint (1, 2)
                            if x == 1:
                                print('lets keep rolling!')
                                keep_rolling = True
                            elif x == 2:
                                print('lets stop rolling!')
                                keep_rolling = False
                                break
                        elif player2score == 21:
                            print('yay i won!!!!')
                            active = False
                            keep_rolling = False
                            break
                        elif player2score > 21:
                            print('Atleast we had fun!')
                            active = False
                            keep_rolling = False
                            break
                elif Bot == 'medium':
                    time.sleep(1)
                    print ('im going to win!')
                    time.sleep(1)
                    while Bot == 'medium':
                        player2score += random.randint(1, 6)
                        time.sleep (1)
                        print(f'Player2score: {player2score}')
                        time.sleep (1)
                        if player2score < 21:
                            if player2score<player1score:
                                print ('i WILL win!')
                                keep_rolling = True
                            elif player2score >= player1score:
                                x = random.randint (1, 2)
                                if x == 1:
                                    print('one more couldnt hurt, right?')
                                    keep_rolling = True
                                elif x == 2:
                                    print('im quitting while ahead.')
                                    keep_rolling = False
                                    break
                        elif player2score == 21:
                            print('I DID IT.')
                            active = False
                            keep_rolling = False
                            break
                        elif player2score > 21:
                            print('GOD. DAMN IT.')
                            active = False
                            keep_rolling = False
                            break
                elif Bot == 'expert':
                    time.sleep(1)
                    print ('I expect nothing but professionalism.')
                    time.sleep(1)
                    while Bot == 'expert':
                        player2score += random.randint(1, 6)
                        time.sleep (1)
                        print(f'Player2score: {player2score}')
                        time.sleep (1)
                        if player2score < 21:
                            if player2score<player1score:
                                print ('I will keep rolling.')
                                keep_rolling = True
                            elif player2score >= player1score:
                                print ('I will stop rolling')
                                keep_rolling = False
                                break
                        elif player2score == 21:
                            print('Oh, how lucky.')
                            active = False
                            keep_rolling = False
                            break
                        elif player2score > 21:
                            print('Oh dear...')
                            active = False
                            keep_rolling = False
                            break
                elif Bot == 'Rigged':
                    time.sleep(1)
                    print ('Playing against the house? Your loss.')
                    time.sleep(1)
                    while Bot == 'Rigged':
                        player2score += random.randint(1, 6)
                        time.sleep (1)
                        print(f'Player2score: {player2score}')
                        time.sleep (1)
                        if player2score < 23:
                            if player2score<player1score:
                                print ('The houses victory is in sight')
                                keep_rolling = True
                            elif player2score >= player1score:
                                print ('The house will stop')
                                keep_rolling = False
                                break
                        elif player2score == 23:
                            print('This game was rigged from the start after all.')
                            active = False
                            keep_rolling = False
                            break
                        elif player2score > 23:
                            print('These dice must be rigged.')
                            active = False
                            keep_rolling = False
                            break
            elif Bot_play == False:
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
                if Bot_play == True:
                    if Bot == 'gambler':
                        print ('you should not be seeing this')
                    elif Bot == 'easy':
                        print ('we had fun!')
                    elif Bot == 'medium':
                        print ('i will find where you live')
                    elif Bot == 'expert':
                        print ('a most honorable game')
                    elif Bot == 'Rigged':
                        print ('You are hereby BANNED from this establishment.')
            elif player2score>player1score:
                print('player2 wins!')
                if Bot_play == True:
                    if Bot == 'gambler':
                        print ('you should not be seeing this')
                    elif Bot == 'easy':
                        print ('Lets play again, again!')
                    elif Bot == 'medium':
                        print ('I win you lose')
                    elif Bot == 'expert':
                        print ('was it even a question?')
                    elif Bot == 'Rigged':
                        print ('havent you heard? the house ALWAYS wins.')
            else:
                print('its a tie!')
                if Bot_play == True:
                    if Bot == 'gambler':
                        print ('you should not be seeing this')
                    elif Bot == 'easy':
                        print ('Tie breaker! Tie breaker!')
                    elif Bot == 'medium':
                        print ('I will win next time')
                    elif Bot == 'expert':
                        print ('Truly a close match')
                    elif Bot == 'Rigged':
                        print ('The house doesnt care for ties.')
    time.sleep(1)
    print (f'player1score = {player1score}')
    time.sleep(1)
    print (f'player2score = {player2score}')
    time.sleep(1)
    print ('game end')

    



