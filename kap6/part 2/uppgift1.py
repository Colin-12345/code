mylist=[]
mylist1=[]

while True:
    x=input('write a number')
    if x=='':
        break
    mylist.append(x)
for c in mylist:
    if c not in mylist1:
        mylist1.append(c)
    else:
        continue
print(', '.join(mylist1))