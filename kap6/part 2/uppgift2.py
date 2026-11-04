station=[]
temp=[]
average=0.0
above_average_indexes=[]
while True:
    s=input('station number and temperature')
    if s == '':
        break
    res=s.rpartition(' ')
    station.append(res[0])
    temp.append(float(res[2]))
for i in range (0, len(temp)):
    if temp[i]>(sum(temp)/len(temp)):
        above_average_indexes.append(i)
print(f'the average temperature was {sum(temp)/len(temp)} degrees \n the stations that were above average are:')
for c in above_average_indexes:
    print (f'station {station[c]} at {temp[c]} degrees')