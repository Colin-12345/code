import random
noun=['cat', 'dog', 'baker', 'baby', 'wife', 'husband'] #the active noun
verb=['meowing', 'barking', 'baking', 'crying', 'sleeping', 'working'] #the verb
noun2=['home', 'work', 'the bakery'] #the passive noun

print(f'the {random.choice(noun)} is {random.choice(verb)} at {random.choice(noun2)}')