def largest(n1, n2, n3):
    nlist=[n1, n2, n3]
    large=0
    for c in nlist:
        if c>large:
            large=c
    return large
print(f'the largest is: {largest(int(input('please input 1st number')), int(input('please input 2nd number')), int(input('please input 3rd number')))}')