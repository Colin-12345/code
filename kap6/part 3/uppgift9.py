kön=[]
for i in range(0, 5):
    kön.append(input('personer i kön'))
while True:
    if len(kön)==0:
        break
    print(f'nu betjänas {kön.pop(0)}!')
    print(kön)
    if input('press enter') == '':
        continue