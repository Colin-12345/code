x=0
y=0
z=0
for i in range (1, 100000000):
    x = int(input('number '))
    if x == 0:
        break
    if x < 0:
        print('negative numbers are ignored')
        continue
    z=x+y
    y=z
print (f'sum {z}')
    