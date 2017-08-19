import random
import sys
from random import shuffle
from random import randint

print('How many weeks?')
weeks = int(input())

def upperME():
    listA = ['1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a', '9a']
    shuffle(listA)

    listB = random.sample(listA, len(listA))

    lengthOfList = int(len(listA))

    if weeks > len(listA):
        diffBetweenListandWeeks = weeks - lengthOfList
    elif weeks == 0:
        sys.exit()
    else:
        diffBetweenListandWeeks = 0

    if diffBetweenListandWeeks > lengthOfList:
        output = listA + listB + listA[:diffBetweenListandWeeks - lengthOfList]
    elif diffBetweenListandWeeks >= 1:
        output = listA + listB[:diffBetweenListandWeeks]
    else:
        output = listA[:weeks]
    print(output)
upperME()

def upperMEacc():
    listA = ['1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a', '9a']
    shuffle(listA)

    listB = random.sample(listA, len(listA))

    lengthOfList = int(len(listA))