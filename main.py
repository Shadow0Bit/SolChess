import WhitePieces as wp
import BlackPieces as bp
from Board import *

print("SolChess \nprototype \nv1.0\n")
checkB, checkW = 1, 1

def selectmode():
    global checkB; global checkW

    select = input("How do you want to play? \nWrite f to play with friend or write AI to play with AI: ")
    if select == "f" or select == "F":
        boardprint()
        while True:
            checkmate()
            if checkB == 0:
                print("White has won the game!")
                break
            elif checkW == 0:
                print("Black has won the game!")
                break

            wp.moves()
            boardprint()

            checkmate()
            if checkB == 0:
                print("White has won the game!")
                break
            elif checkW == 0:
                print("Black has won the game!")
                break

            bp.moves()
            boardprint()

    elif select == "AI" or select == "ai":
        print("You fool, there is no AI mode yet")
    else:
        print("Wtf are you saing to me?")
        selectmode()


def checkmate():
    global checkB
    global checkW
    for i in range(0, 8):
        try:
            board[i].index(" K ")
            checkB = 1
            break
        except:
            checkB = 0

    for i in range(0, 8):
        try:
            board[i].index(" k ")
            checkW = 1
            break
        except:
            checkW = 0

selectmode()