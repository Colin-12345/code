numbers = []
for i in range (1, 100000000000):
    x=input(f'number {i}: ')
    numbers.append(int(x))
    if x == '0':
        break

print(sum(numbers))