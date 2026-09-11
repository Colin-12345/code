x=0 #positive
y=0 #negative
w= 0 #biggest
numbers = []
for i in range (1, 100000000000000):
    z=int(input('number '))
    if z == 0:
        break
    numbers.append(int(z))
    if z > 0:
        x+=1
    elif z < 0:
        y+=1
    if z > w:
        w = z
print (f'you entered {x} positive numbers and {y} negative numbers')
print (f'the sum of all the numbers is {sum(numbers)}')
print (f'the biggest number you entered was {w}')