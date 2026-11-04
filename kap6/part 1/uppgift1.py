mylist=['2']
for i in range (0, int(input('how many numbers do you want?'))-1):
    mylist.append(str(int(mylist[-1])+3))
print(', '.join(mylist))