mylist=['red', 'green', 'blue']
newlist=[]
for c in mylist:
    if c == 'green':
        newlist.append(input('input a new color'))
    else:
        newlist.append(c)
print (f'{mylist} \n{newlist}')