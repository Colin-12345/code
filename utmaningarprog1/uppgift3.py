import random
x = int(input('input lower bound '))
y = int(input('input upper bound '))
z = int(input('how many numbers should be generated?'))
numbers=[]
for i in range (0, z):
    numbers.append(random.randint(x, y))

outputlist=[]
output=''
for i in range(0, z):
    outputlist.append(str(numbers[i]))
    if i % 5 == 4:
        outputlist.append('\n')
belowaverage=0
output=' '.join(outputlist)
print(f" {output}\nthe average of the numbers was: {sum(numbers)/len(numbers)}")
for c in numbers:
    if c < sum(numbers)/len(numbers):
        belowaverage+=1
print(f"the amount that fell below that line is {belowaverage}")
