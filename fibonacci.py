def fibonacci(n):
    x=n
    y=0
    z=1
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        for i in range (0, x-1):
            w=z+y
            y=z
            z=w
        return z

print(fibonacci(int(input('number '))))