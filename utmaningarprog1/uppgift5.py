import random
x=random.randint(1,10) #random A argument
y=random.randint(1,10) #random B argument
correct=False
for i in range (1,5):
    z=int(input(f'{x}*{y}='))
    if z == x*y:
        correct=True
        break
    else:
        print(f'wrong answer, {5-i} attempts remaining')
if correct == True:
    print('correct answer!')
else:
    print(f'you are stupid\nthe answer was {x*y}')