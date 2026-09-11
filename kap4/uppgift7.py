numbers = []
positiva_number=0
for i in range(1, 11):
    numbers.append(int(input(f'number ')))
for i in range(0, 10):
    if numbers[i] >= 0:
        positiva_number+=1

print (f'you entered {positiva_number} positive numbers')
