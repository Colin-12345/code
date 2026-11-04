mylist=['']
for i in range (0, 5):
    mylist.append(input('input words'))
mylist.sort()
print (f'{mylist[1:len(mylist)]} \n{mylist[len(mylist):0:-1]}')