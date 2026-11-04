mylist=[]
while True:
    x=input('input numbers')
    if x == '':
        break
    y=int(x)
    mylist.append(y)
mylist.sort()
for i in range (0, len(mylist)):
    if i<len(mylist)/2:
        continue
    elif i==len(mylist)/2:
        print(f'the median is {(mylist[i-1]+mylist[i])/2}')
        break
    elif i>len(mylist)/2:
        print(f'the median is {mylist[i-1]}')
        break
        
