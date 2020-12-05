# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from random import randint

youngerage = 5

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def birthday(age):
    olderage = age + 4
    print(olderage)


def randomWinner():
    rando = randint(1, 95)

    if rando > 50:
        print("Mark is da wiiiiinaaaar")
    elif rando == 30:
        print("rando equals 30")
    else:
        print("Tara is THE WINNER!!!!!")

randomWinner()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

