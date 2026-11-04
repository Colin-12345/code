mylist=[]
mytuple=('1', '2', '3', '4', '5',)
print(f'tuple: {mytuple}')
while True:
    x=input('input into list')
    if x == '':
        break
    mylist.append(x)
temp=list(mytuple)
if mylist == temp:
    print('the tuple and list are the same')
else:
    print('the tuple and list are not the same')