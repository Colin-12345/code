import random
x=random.randint(1,100)

for i in range (1, 1000000000):
    guess=int(input('guess number '))
    if guess < x:
        print ('too low')
    elif guess > x:
        print ('too high')
    else:
        print ('you guessed it!')
        break