outputlist=[]
output=''
for i in range(1,11):
    outputlist.append('\n')
    for k in range (0, 11):
        outputlist.append(f"\t{k*i}")
output= ' '.join(outputlist)
print (output)