x=int(input('number to count '))

for i in range (1, x+1):
    if i % 2 == 0:
        print (f'{i} is even')
    else:
        print (f'{i} is odd')