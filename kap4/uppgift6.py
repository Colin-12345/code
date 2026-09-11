numbers=[]
for i in range (1, 6):
    numbers.append(int(input(f'number ')))
for i in range (0, 5):
    if numbers[i] > 0:
        print (f'{numbers[i]} is positive')
    elif numbers[i] < 0:
        print (f'{numbers[i]} is negative')
    else:
        print (f'{numbers[i]} is zero')