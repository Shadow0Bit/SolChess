import WhitePieces as w
import BlackPieces as b
from Board import *

while True:
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

    if checkB == 0:
        print("White has won the game!")
        break
    elif checkW == 0:
        print("Black has won the game!")
        break
    else:
        pass

    w.moves()
    b.moves()