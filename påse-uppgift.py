#the variables
påse=[]
templist=[]
active=True
search=''
choice=''
amount=0

#the main loop
while active: 
    #the user input
    choice=input("""please choose an option.
    [V] show contents of the bag.
    [S] put something in the bag.
    [F] search for something in the bag.
    [T] take something out of the bag.
    [A] sort the bag.
    [Q] stop the progam. """).lower()
    if choice=='v': #prints the list converted to a string
        print(', '.join(påse))

    elif choice=='s': #puts an item in the bag
        påse.append(input('what do you want to put in the bag? '))
        print('item added')

    elif choice=='f': #searches for an item in the bag
        search=input('what do you want to search for? ')
        if search in påse:
            print(f'you rummage around and find {search}')
        else:
            print(f'try as you might, you just cant find {search}')

    elif choice=='t': #gets rid of a chosen amount of copies of an item in the bag
        templist=[]
        search=input('what do you want to get rid of? ')
        if search in påse:
            amount=påse.count(search)
            if amount==1:
                amount=1
            else: #if there are multiple of the same item in the bag
                amount=int(input(f'found {amount} iterations, how many do you want to get rid of? '))
            for i in range (0, len(påse)): #main loop that gets rid of the chosen amount of items
                if påse[i]==search and amount!=0:
                    amount -= 1
                    continue
                else:
                    templist.append(påse[i])
            påse=templist.copy()
            print(f'you diligently remove {search} from the bag')
        else: #incase you try and get rid of something that isnt there
            print('try as you might, you can not get rid of something that isnt there.')

    elif choice=='a': #sorts the bag
        if len(påse)<=1 or påse == sorted(påse):
            print('no need, its already sorted')
        else:
            påse.sort()
            print('you diligently take all the items out and put them back in alphabetical order')

    elif choice=='q': #ends the program
        print('thank you for using the bag service.')
        active=False
        break

    else: #incase you are too dumb to read
        print('invalid input, try again')