mylist=[]
mylist1=[]
while True:
    x=(input('input a number, or input any letter to stop inputting '))
    try:
        y=int(x)
    except ValueError:
        break
    else:
        mylist.append(y)
for c in mylist:
    if c == 0:
        continue
    else:
        mylist1.append(str(c))
print(', '.join(mylist1))