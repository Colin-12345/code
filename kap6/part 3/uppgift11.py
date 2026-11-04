import random
mylist=[]
even=[]
odd=[]
for i in range (0, 20):
    mylist.append(random.randint(1, 50))
for c in mylist:
    if c%2==0:
        even.append(c)
    elif c%2==1:
        odd.append(c)
print(f'{mylist}\neven:\t{even} \nodd:\t{odd}')