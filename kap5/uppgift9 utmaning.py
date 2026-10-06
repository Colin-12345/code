import sys
personnummer = str(input('sätt in ditt personnummer '))
memory = ''
temp1=''
temp2=''
temp3=''
temp4=[]
sumresult=0
result=''

#length and hyphen check
temp1 = list(personnummer)
if '-' not in temp1:
    print('snälla ha ett sträck (-) mellan födelsedatum och personligt nummer')
    sys.exit()
if len(personnummer)<11:
    print('personnummer är 10 siffror med ett sträck (-) mellan födelse datum och personligt number')
    sys.exit()

    

#gets rid of '-'
for c in personnummer:
    if c=='-':
        continue
    else:
        temp2 += c
memory = temp2

#makes every number operateable
temp1 = list(temp2)
temp1[-1] = ''
temp2 = ''.join(temp1)
temp1 = list(temp2)

#double every number intermittently
for i in range (0, len(temp1)):
    if i % 2 == 0:
        temp4.append(str(int(temp1[i])*2))
    elif i % 2 == 1:
        temp4.append(str(int(temp1[i])))

#turning every 2 digit number into 2 1 digit numbers
temp3=''.join(temp4)
temp4=list(temp3)

#summing every digit
for c in temp4:
    sumresult+=int(c)

#getting the control digit
for i in range (0, 10000000000):
    if (10*i)-sumresult <0:
        continue
    else:
        result=(10*i)-sumresult
        break

#controlling if it actually was a personnummer
temp1.append(str(result))
temp2 = ''.join(temp1)
if temp2==memory:
    print('aktuellt personnummer')
else:
    print('icke aktuellt personnummer')


