mystring=input('please input a sentence')
mylist=mystring.split()
myset=set()
output=''
for c in mylist:
    if c not in myset:
        myset.add(c)
        output+= c
        amount=mylist.count(c)
        output+= ' '
        output+= str(amount)
        output+= '\n'
    else:
        continue
print (output)