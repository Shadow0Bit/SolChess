import WhitePieces as w
import BlackPieces as b
from Board import *

print("SolChess \nprototype \nv1.0\n")
checkB, checkW = 1, 1

def selectmode():
    global checkB; global checkW

    select = input("How do you want to play? \nWrite f to play with friend or write AI to play with AI: ")
    if select == "f" or select == "F":
        while True:
            checkmate()
            if checkB == 0:
                print("White has won the game!")
                break
            elif checkW == 0:
                print("Black has won the game!")
                break

            w.moves()

            checkmate()
            if checkB == 0:
                print("White has won the game!")
                break
            elif checkW == 0:
                print("Black has won the game!")
                break

            b.moves()

    elif select == "AI" or select == "ai":
        print("You fool, there is no AI mode yet")
    else:
        print("Wtf are you saing to me?")
        selectmode()


def checkmate():
    global checkB;
    global checkW
    for i in range(0, 7):
        try:
            board[i].index(" K ")
            checkB = 1
            break
        except:
            checkB = 0

        try:
            board[i].index(" k ")
            checkW = 1
            break
        except:
            checkW = 0




selectmode()