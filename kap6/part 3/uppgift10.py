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
if input('do you have a word in mind to count? (y/n)') == 'y':
    x= input('what is the word you want?')
    output = x
    output += f' {mylist.count(x)}'
print (output)