outputlist=[]
output=''
for i in range(1,11):
    outputlist.append('\n')
    for k in range (0, 11):
        outputlist.append(f"{k*i}")
output= '\t'.join(outputlist)
print (output)

mylist=['string 1', 'string 2']
for i in range (0, len(mylist)):
    print()
    for j in range (0, len(mylist[i])):
        print((mylist[i])[j])