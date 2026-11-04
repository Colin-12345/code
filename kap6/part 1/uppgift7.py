m = []
while True:
    s = input('? ')
    if s == '':
        break
    ls = s.split(',')
    rad = [float(e) for e in ls]
    m.append(rad)
print(m)
print(ls)