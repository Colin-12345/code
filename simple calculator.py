x = int(input('numberA: '))
y = int(input('numberB: '))

print('1=add ')
print('2=subtract ')
print('3=multiply ')
print('4=divide ')
operator = int(input('enter operator: '))
if operator == 1:
    print (f'{x+y}')
elif operator == 2:
    print (f'{x-y}')
elif operator == 3:
    print (f'{x*y}')
elif operator == 4:
    print (f'{x/y}')
else:
    print ('syntax error')
