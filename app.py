import os
import random
import time
from utils import whitetext, greentext

ANSWERS = ['it is certain', 'it is decidedly so', 'it is without a doubt', 'yes, definitely', 'you may rely on it',
           'as I see it, yes', 'it is most likely', 'the outlook is good', 'yes, signs point to yes',
           'you shouldn\'t count on it', 'my reply is no', 'my sources say no', 'the outlook is not so good',
           'it is very doubtful']
ANSWERS_LENGTH = len(ANSWERS) - 1


def clear():
    if os.name != 'nt':
        os.system('clear')
        return

    os.system('cls')


def magic8ball():
    time.sleep(random.randint(1, 2))
    greentext(f'\n{ANSWERS[ANSWERS_LENGTH]}')


def continue8ball():
    whitetext('\nWould you like to ask me another question?')
    ask_again = input().lower().strip()

    if ask_again != 'yes':
        print('Are you sure?')
        sure = input().lower().strip()

        if sure == 'yes':
            clear()
            exit()

    whitetext('Ok, ask me another yes or no question!')
    input()
    magic8ball()

    continue8ball()


def loadingscreen(num, stop):
    if num <= stop:
        greentext('Loading... 0%')
        time.sleep(1)
        clear()
        return

    greentext(f'Loading... {num}%')

    time.sleep(random.randint(60, 100) / 100)
    loadingscreen(num - random.randint(4, 11), stop)

