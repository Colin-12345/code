namn=[]
pris=[]
minimal=200000000
minimal_index=0
while True:
    s=input('namn och pris, ha ett blanksteg mellan namn och pris, skriv inget för att sluta ')
    if s == '':
        break
    res=s.rpartition(' ')
    namn.append(res[0])
    pris.append(float(res[2]))
for i in range (0, len(pris)-1):
    if pris[i]<minimal:
        minimal=pris[i]
        minimal_index=i
print(f'den med lägsta kostnad är {namn[minimal_index]} med kostnad {minimal}kr')
