vowels = ['a', 'e', 'i', 'o', 'u', ' ', ',', '.', '?', '!']
output = ''

x=input(str('input a string to translate to piratespeak'))

for c in x:
    if c in vowels:
        output += c
    else: 
        output += (c+'o'+c)
print (output)


