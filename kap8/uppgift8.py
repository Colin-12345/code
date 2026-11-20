def average(numlist):
    total=0
    for c in numlist:
        total+=int(c)
    ave=total/len(numlist)
    return ave
print(average(str(input('please input a list of numbers separated by a comma and space. ')).split(', ')))