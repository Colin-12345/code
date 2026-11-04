
mylist=[]
Negative_count=0
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
    if c<0:
        Negative_count+=1
    mylist1.append(str(c))

print(f'the numbers you inputted were: {', '.join(mylist1)} \n{Negative_count} were below zero')