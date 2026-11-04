import random
random_numbers=[]
lowest=1001
highest=0
average=0
for i in range (0, 100):
    random_numbers.append(random.randint(1, 1000))
for c in random_numbers:
    if c>highest:
        highest=c
    elif c<lowest:
        lowest=c
average=sum(random_numbers)/len(random_numbers)
print(f"lowest: {lowest}\n highest: {highest}\naverage: {average}")