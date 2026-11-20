def menu(title, option1, option2):
    print (f"""*** {title} ***
-----------------
1. {option1}
2. {option2}""")
    x=''
    return x

print(menu('startmeny', 'spela', 'inställningar'))
print(menu('inställningar', 'ljud', 'grafik'))
print(menu('highscore', 'Anna - 500p', 'Bo - 320p'))
    