x=input(str('input text with spaces '))
string = ''
for i in range (0, (len(x))):
    if x[i] == ' ':
        continue
    else:
        string+=(x[i])
print (string)
