# skapa en 10x10 multiplikationstabell
a = []
x=int(input('hur lång ska tabellen vara? '))
y=int(input('hur hög ska tabellen vara? '))
for i in range(0, y):
    a.append('\n')
    for j in range(0, x):
        a.append(str((j+1)*(i+1)))
print('\t'.join(a))