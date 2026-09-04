password = ('Python')
x = input('enter your password: ')
if x == password:
    print('correct password')
elif len(x) <= 3:
    print('password is too short')
else:
    print('wrong password')