import random

def hangman(word):
    wrong = 0
    stages = ["",
               "_____________________",
               "|                    ",
               "|          |         ",
               "|          0         ",
               "|         /|\        ",
               "|         / \        ",
               "|                    ",

              ]

    rletters = list(word)
    board = ["__"]*len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) - 1 :
       print("\n")
       msg = "Guess a letter: "
       char = input(msg)
       if char in rletters:
            cind = rletters.index(char)
            board[cind]=char
            rletters[cind] = '$'
       else:
           wrong += 1
       print((" ".join(board)))
       e = wrong + 1
       print("\n".join(stages[0:e]))
       if "__" not in board:
            print("you win!!")
            print("  ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}".format(word))

def main():
    value = random.randrange(0,3)
    print("random number: {} ".format(value))
    words =["cat","dog","ant"]
    word = words[value]
    hangman(word)

if __name__ == "__main__":
    main()