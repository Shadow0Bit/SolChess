from Board import *


def moves():
    boardprint()
    userinput = input("Coordinates: ")
    position(userinput[0], userinput[-1])
    pawn()
    rook()
    knight()

def move(a, b):
    global mx
    global my
    if a == "a":
        mx = 0
    elif a == "b":
        mx = 1
    elif a == "c":
        mx = 2
    elif a == "d":
        mx = 3
    elif a == "e":
        mx = 4
    elif a == "f":
        mx = 5
    elif a == "g":
        mx = 6
    elif a == "h":
        mx = 7
    else:
        print("Try something else")
    if b == "8":
        my = 0
    elif b == "7":
        my = 1
    elif b == "6":
        my = 2
    elif b == "5":
        my = 3
    elif b == "4":
        my = 4
    elif b == "3":
        my = 5
    elif b == "2":
        my = 6
    elif b == "1":
        my = 7
    else:
        print("Try something else")


def position(a, b):
    global x
    global y
    global mx
    global my
    if a == "a":
        x = 0
    elif a == "b":
        x = 1
    elif a == "c":
        x = 2
    elif a == "d":
        x = 3
    elif a == "e":
        x = 4
    elif a == "f":
        x = 5
    elif a == "g":
        x = 6
    elif a == "h":
        x = 7
    else:
        print("Try something else")
    if b == "8":
        y = 0
    elif b == "7":
        y = 1
    elif b == "6":
        y = 2
    elif b == "5":
        y = 3
    elif b == "4":
        y = 4
    elif b == "3":
        y = 5
    elif b == "2":
        y = 6
    elif b == "1":
        y = 7
    else:
        print("Try something else")
    if board[y][x] == " p " or board[y][x] == " r " or board[y][x] == " h " \
            or board[y][x] == " b " or board[y][x] == " q " or board[y][x] == " k ":
        pass
    else:
        print("Try something else")
        position(input("First coordinate: "), input("Second coordinate: "))


def pawn():
    global x; global y; global mx; global my

    if board[y][x] == " p ":
        userinput = input("Write where you want to move: ")
        move(userinput[0], userinput[-1])
        if x == mx:
            if y > 0:
                if y == 6 and my == 4:
                    for i in range(5, 3, -1):
                        print("!")
                        if board[i][x] == " . ":
                            board[i][x] = " p "
                            i += 1
                            board[i][x] = " . "
                        else:
                            i += 1
                            if i == y or board[i][x] != " . ":
                                print("Try something else")
                                moves()
                            else:
                                board[y][x] = " . "
                                board[i][x] = " p "
                                break
                else:
                    i = y - 1
                    if board[i][x] == " . " and i == my:
                        board[y][x] = " . "
                        board[i][x] = " p "
                    else:
                        print("Try something else")
                        moves()
        elif x != mx and y > my and board[my][mx] != " p " and board[my][mx] != " r " and board[my][mx] != " h " \
                    and board[my][mx] != " b " and board[my][mx] != " q " and board[my][mx] != " k ":
            ay = y - 1
            if ay == my:
                ax = x - 1
                if mx == ax:
                    board[my][mx] = " p "
                    board[y][x] = " . "
                else:
                    ax = x + 1
                    if mx == ax:
                        board[my][mx] = " p "
                        board[y][x] = " . "
                    else:
                        print("Try something else")
                        moves()
        else:
            print("Try something else")
            moves()
        boardprint()

    else:
        pass


def rook():
    global x; global y; global mx; global my

    if board[y][x] == " r ":
        userinput = input("Write where you want to move: ")
        move(userinput[0], userinput[-1])
        if mx == x and my != y:
            if y < my:
                a = y + 1
                b = my + 1
                c = 1
            if y > my:
                a = y - 1
                b = my - 1
                c = -1
            for i in range(a, b, c):
                if board[i][x] == " p " or board[i][x] == " r " or board[i][x] == " h " \
                    or board[i][x] == " b " or board[i][x] == " q " or board[i][x] == " k ":
                    if not li == y:
                        board[li][x] = " r "
                        board[y][x] = " . "
                        break
                    else:
                        print("Try something else")
                        moves()
                elif board[i][x] == " . ":
                    if i == my:
                        board[i][x] = " r "
                        board[y][x] = " . "
                        break
                    else:
                        pass
                else:
                    board[i][x] = " r "
                    board[y][x] = " . "
                    break
                li = i
        elif mx != x and my == y:
            if x < mx:
                a = x + 1
                b = mx + 1
                c = 1
            if x > mx:
                a = x - 1
                b = mx - 1
                c = -1
            for i in range(a, b, c):
                if board[y][i] == " p " or board[y][i] == " r " or board[y][i] == " h " \
                    or board[y][i] == " b " or board[y][i] == " q " or board[y][i] == " k ":
                    if not li == x:
                        board[y][li] = " r "
                        board[y][x] = " . "
                        break
                    else:
                        print("Try something else")
                        moves()
                elif board[y][i] == " . ":
                    if i == mx:
                        board[y][i] = " r "
                        board[y][x] = " . "
                        break
                    else:
                        pass
                else:
                    board[y][i] = " r "
                    board[y][x] = " . "
                    break
                li = i
        boardprint()
    else:
        pass


def knight():
    pass
