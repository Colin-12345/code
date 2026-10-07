lifeline = [
r"""
 ♥ ♥ ♥ ♥ ♥ ♥
      O
     /|\
     / \
""",
r"""
 ♥ ♥ ♥ ♥ ♥
      O
     /|\
     / \
""",
r"""
 ♥ ♥ ♥ ♥
      O
     /|\
     / \
""",
r"""
 ♥ ♥ ♥
      O
     /|\
     / \
""",
r"""
 ♥ ♥
      O
     /|\
     / \
""",
r"""
 ♥
      O
     /|\
     / \
""",
r"""
      
      O
     /|\
     / \
"""
]
lives=6
wordtoguess=str(input('please input a word for player 2 to guess '))
wordletters= set(wordtoguess)
guessedletters = []
guessedletters_set = set(guessedletters)
guessedwordlist=[]
active = True
while active == True:
     guessedword=''
     guessedwordlist=list(guessedword)
     print(lifeline[6-lives])
     for c in wordtoguess:
          if c in guessedletters:
               guessedwordlist.append(c)
          else:
               guessedwordlist.append('_')
     guessedword=''.join(guessedwordlist)
     print(guessedword)
     if guessedword == wordtoguess:
          print('you win!')
          active =False
          break
     if lives==0:
          print('you lose :(')
          active=False
          break
     print(guessedletters)
     for i in range (0, 10000):
          x = str(input('guess a letter '))
          if len(x) >1:
               print('please only guess 1 letter')
               continue
          elif len(x) <=0:
               print('please input a letter')
               continue
          elif x in guessedletters:
               print('that letter has already been guessed')
               continue
          else:
               guessedletters.append(x)
               if x in wordletters:
                    break
               elif x not in wordletters:
                    lives-= 1
                    break
     guessedletters_set=set(wordletters)