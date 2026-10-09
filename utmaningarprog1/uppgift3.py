import random
x = int(input('input lower bound ')) #lower bound
y = int(input('input upper bound ')) #upper bound
z = int(input('how many numbers should be generated?')) #amount generated
numbers=[] #list of numbers
for i in range (0, z):
    numbers.append(random.randint(x, y)) #adds numbers to the list

outputlist=[] #the operateable output
output='' #the outputting output
for i in range(0, z):
    outputlist.append(str(numbers[i])) #moves from list to output
    if i % 5 == 4:
        outputlist.append('\n') #adds a new line to output
belowaverage=0 #how many numbers are below average
output=' '.join(outputlist)
print(f"these are the numbers:\n {output}\nthe average of the numbers was: {sum(numbers)/len(numbers)}")
for c in numbers:
    if c < sum(numbers)/len(numbers):
        belowaverage+=1
print(f"the amount that fell below that line is {belowaverage}")
