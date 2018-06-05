import random

def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
             ]
    rletters = list(word.upper())
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter:"
        char = input(msg).upper()
        if char in rletters:
            cind = rletters.index(char)
            rletters[cind] = "$"
            board[cind] = char
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print(" ".join(board))
            win = True
            break
    if win == True:
        print("You Won!")
    else:
        print("You Lost. \nThe Answer was {}".format(word))


word_list = ["Java", "Python", "Ruby", "C++", "React", "CSS"]
random_index = random.randint(0, len(word_list))
hangman(word_list[random_index])
