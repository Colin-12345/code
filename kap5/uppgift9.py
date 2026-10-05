x = input(str('input a string to check '))
string1=''
string2=''
for i in range (0, (len(x))):
    if x[i] == ' ':
        continue
    else:
        string1+=(x[i])
string2=(string1[len(string1):0:-1])
string2+=(string1[0])
if string1==string2:
    print('that string is a palindrome!')
    print(string1)
    print(string2)
else:
    print('that string is NOT a palindrome!')
    print(string1)
    print(string2)