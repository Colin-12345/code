y=0
x=0
for i in range (1, 6):
    x = int(input(f'number {i}: '))
    if x > y:
        y = x

print (f'largest number is {y}')