from search import *
import random

def make_rand_8puzzle():
    spots = (0, 1, 2, 3, 4, 5, 6, 7, 8)

    notcompleted = True
    while notcompleted:
        initial = random.sample(spots,9)
        eightwall = EightPuzzle(initial)
        if eightwall.check_solvability(eightwall.initial):
            return eightwall



def display(state):
    for i in range(0,3):
        if (state[i] == 0):
            print ("*", end= " ")
        else:
            print (state[i], end=" ")
    print()
    for i in range(3,6):
        if (state[i] == 0):
            print ("*", end= " ")
        else:
            print (state[i], end=" ")
    print()
    for i in range (6,9):
        if (state[i] == 0):
            print ("*", end= " ")
        else:
            print (state[i], end=" ")
    print()


eightPuzzle = make_rand_8puzzle()
display(eightPuzzle.initial)


