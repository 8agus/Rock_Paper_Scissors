import random


def yes_or_no():
    you_want = str(input("You want to play? (yes/no): "))
    if you_want == "yes":
        print("Great, lets go")
    while you_want.lower() != "yes":
        print('Okay, maybe next time')
        exit()


def selection():
    choice = str(input("Choose R for Rock, P for Paper or S for Scissors :"))
    print("You have selected {}".format(choice.upper()))
    return choice.upper()


def pc_select():
    pc_options = ["R", "P", "S"]
    pc_choice = random.choice(pc_options)
    print("PC selected {}".format(pc_choice))
    return pc_choice


def who_wins(q2, pc):

    if pc == 'R' and q2 == 'P':              # Rock and Paper
        return "Player wins!!"
    elif pc == 'P' and q2 == 'R':
        return "PC wins!!"
    elif pc == 'R' and q2 == 'S':            # Rock and Scissor
        return "Pc wins!!"
    elif pc == 'S' and q2 == 'R':
        return "Player wins!!"
    elif pc == 'P' and q2 == 'S':            # Paper and Scissor
        return "Player wins!!"
    elif pc == 'S' and q2 == 'P':
        return "PC wins!!"
    if pc == q2:
        return "It is a draw"

