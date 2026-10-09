import random
import string
wordlist=[]
word=''
tries=5
guesses=''
for i in range(0,5):
    wordlist.append(random.choice(string.ascii_lowercase))
word=wordlist
while True:
    if tries==0:
        print(f'you lose \nthe word was {word}')
        break
    print(f'{tries} tries left')
    guess=str(input('please guess a word '))
    if len(guess)!=5:
        print('please guess a 5 letter word')
        continue
    if guess==word:
        print('you win!')
        break
    if tries==0:
        print(f'you lose \nthe word was {word}')
        break
    tries-=1
    guesslist=list(guess)
    guesses=''
    for i in range (0, len(guesslist)):
        if guesslist[i]==wordlist[i]:
            guesses+='g'
        elif guesslist[i] in wordlist:
            guesses+='y'
        else:
            guesses+='r'
    print(guess)
    print(guesses)