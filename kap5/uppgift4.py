s=input(str('skriv en sträng '))
currentlast=0
finnsvitt=0
i=0
for c in s:
    if c==' ':
        currentlast=i
        finnsvitt=1
    i+=1
if finnsvitt==1:
    print(f'sista vit tecken finns på index nr. {currentlast}')
else:
    print('finns inget vit-tecken')