attempts=0
for i in range (1, 1000): 
    if 'python123' == input('password '):
        print ('correct password')
        break
    elif attempts == 2:
        print ('too many failed attempts')
        break
    else:
        attempts += 1
        print ('wrong password')