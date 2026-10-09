import random
players=[]
team1=[]
team2=[]
active= True
while active == True:
    x=str(input('please input the players, press 2 to finish inputting')) #input
    if x=='2':
        active==False
        break
    else:
        players.append(x)
        continue
for i in range(0, len(players)):
    if len(team1)>len(players)/2: #makes sure teams are even
        team2.append(players[i])
    elif len(team2)>len(players)/2:
        team1.append(players[i])
    x=random.randint(1, 2)
    if x == 1: #random assignment
        team1.append(players[i])
    elif x == 2:
        team2.append(players[i])
print(f"team1:{', '.join(team1)}\nteam2:{', '.join(team2)}")
