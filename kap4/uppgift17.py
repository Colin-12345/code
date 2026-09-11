for i in range (1, 1000000000000):
    print ('option 1: count')
    print ('option 2: multiplication table')
    print ('option 3: end')
    x = int(input('choose option '))
    if x == 1:
        y = int(input('number to count to'))
        for i in range (1, y+1):
            print (i)
    elif x == 2:
        y = int(input('number'))
        for i in range (0, 10):
            print (f'{y} * {i+1} = {y*(i+1)}')
    elif x == 3:
        break
    else:
        print ('syntax error')
        