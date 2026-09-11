x = int(input('number to count '))
for i in range (1, x+1):
    if i % 3 == 0:
        continue
    print (i)