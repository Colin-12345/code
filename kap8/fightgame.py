import random
import time
def show_status(P_hp, M_hp):
    print(f"Player: {P_hp} | Monster hp: {M_hp} \n")

def show_menu():
    print("""options:
1. Sword slash  (15-20 damage, 100% accuracy)
2. fireball     (25-35 damage,  50% accuracy)
3. Heal         (15-25 heal)""")
    
def player_turn(choice):
    damage=0
    if choice == 1:
        damage=15+random.randint(0, 5)
        print(f'You slash at the monster, dealing {damage} damage.')
    elif choice == 2:
        print('You channel your magic')
        for i in range (0, 3):
            time.sleep(0.5)
            print('.')
        time.sleep(0.5)
        accuracy=random.randint(1, 2)
        if accuracy==1:
            print('Your magic misses, bummer.')
        elif accuracy==2:
            damage=25+random.randint(0,10)
            print(f'Direct hit! You deal {damage} damage.')
    elif choice == 3:
        damage=-15-random.randint(0, 10)
        print('You channel your magic to heal, ')
        time.sleep(0.5)
        print(f'You heal {damage*-1} health')
    else:
        print('You tried to do something really cool, but failed. Maybe do something you know how to do.')
    return damage
def monster_turn():
    damage=10+random.randint(0, 15)
    print(f'The monster swings at you, dealing {damage} damage.')
    return damage

monsterhp=200
playerhp=100

while True:
    print('You are in the middle of fighting a monster. \n')
    if playerhp>100:
        playerhp=100
    if monsterhp>200:
        monsterhp=200
    time.sleep(1)
    show_status(playerhp, monsterhp)
    time.sleep(1)
    show_menu()
    time.sleep(1)
    damage= player_turn(int(input('What do you want to do? ')))
    if damage >=0:
        monsterhp=monsterhp-damage
    elif damage <0:
        playerhp=playerhp-damage
    time.sleep(1)
    if monsterhp<=0:
        print('The monster has been felled! You win!')
        break
    print()
    damage=monster_turn()
    playerhp=playerhp-damage
    time.sleep(1)
    if playerhp<=0:
        print('You have been defeated in combat... You lose.')
        break
