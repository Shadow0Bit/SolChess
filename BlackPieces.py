from Board import *

check, check2, check3, check4, check5, check52 = 0, 0, 0, 0, 0, 0
# Check = | rook, Check2 = -- rook, Check3 = \ bishop, Check4 = / bishop, Check5 = \ pawn, Check52 = / pawm
def kingcheck():
    global check; global check2; global check3; global check4; global check5; global check52

    for y in range(0, 8):
        try:
            x = board[y].index(" K ")    # Check King Position
            break
        except:
            pass
    for i in range(y + 1, 8):
        if board[i][x] == " r " or board[i][x] == " q ":
            print("Check!")
            check = 1
            break
        elif board[i][x] == " . ":
            pass
        else:
            break
    for i in range(y - 1, -1 , -1):
        if board[i][x] == " r " or board[i][x] == " q ":
            check = 1
            break
        elif board[i][x] == " . ":
            pass
        else:
            break

    for i in range(x + 1, 8):
        if board[y][i] == " r " or board[y][i] == " q ":
            check2 = 1
            break
        elif board[y][i] == " . ":
            pass
        else:
            break
    for i in range(x - 1, -1 , -1):
        if board[y][i] == " r " or board[y][i] == " q ":
            check2 = 1
            break
        elif board[y][i] == " . ":
            pass
        else:
            break

    ax = x
    for i in range(y + 1, 8):
        ax += 1
        if ax > 7 or ax < 0:
            break
        if board[i][ax] == " b " or board[i][ax] == " q ":
            check3 = 1
            break
        elif board[i][ax] == " . ":
            pass
        else:
            break
    ax = x
    for i in range(y - 1, -1, -1):
        ax -= 1
        if board[i][ax] == " b " or board[i][ax] == " q ":
            check3 = 1
            break
        elif board[i][ax] == " . ":
            pass
        else:
            break
    ax = x
    for i in range(y + 1, 8):
        ax -= 1
        if board[i][ax] == " b " or board[i][ax] == " q ":
            check4 = 1
            break
        elif board[i][ax] == " . ":
            pass
        else:
            break
    ax = x
    for i in range(y - 1, -1, -1):
        ax += 1
        if ax > 7 or ax < 0:
            break
        if board[i][ax] == " b " or board[i][ax] == " q ":
            check4 = 1
            break
        elif board[i][ax] == " . ":
            pass
        else:
            break
    if y > 0 and x > 0:
        if board[y + 1][x - 1] == " p ":
            check5 = 1
    if y > 0 and x < 7:
        if board[y + 1][x + 1] == " p ":
            check52 = 1


def moves():
    print("It's black turn (uppercase letters)")
    userinput = input("Write coordinates of the piece you want to move: ")
    position(userinput[0], userinput[-1])
    checkifdot()
    pawn()
    rook()
    horse()
    bishop()
    queen()
    king()


# Move coordinate converter
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

# Position coordinate converter
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
    if board[y][x] == " P " or board[y][x] == " R " or board[y][x] == " H " \
            or board[y][x] == " B " or board[y][x] == " Q " or board[y][x] == " K ":
        pass
    else:
        print("Try something else")
        userinput = input("Write coordinates of the piece you want to move: ")
        position(userinput[0], userinput[-1])


def pawn():
    global x; global y; global mx; global my

    if board[y][x] == " P ":
        piece = board[y][x]
        userinput = input("Write where you want to move: ")
        move(userinput[0], userinput[-1])
        if x == mx:
            if y < 8:
                if y == 1 and my == 3:
                    for i in range(y + 1, 4):
                        if board[i][x] == " . ":
                            board[i][x] = piece
                            i -= 1
                            board[i][x] = " . "
                        else:
                            i -= 1
                            if i == y or board[i][x] != " . ":
                                print("Try something else")
                                moves()
                            else:
                                board[y][x] = " . "
                                board[i][x] = piece
                                break
                else:
                    i = y + 1
                    if board[i][x] == " . " and i == my:
                        board[y][x] = " . "
                        board[i][x] = piece
                    else:
                        print("Try something else")
                        moves()
        elif x != mx and y < my and board[my][mx] != " P " and board[my][mx] != " R " and board[my][mx] != " H " \
                    and board[my][mx] != " B " and board[my][mx] != " Q " and board[my][mx] != " K ":
            ay = y + 1
            if ay == my:
                ax = x - 1
                if mx == ax:
                    board[my][mx] = piece
                    board[y][x] = " . "
                else:
                    ax = x + 1
                    if mx == ax:
                        board[my][mx] = piece
                        board[y][x] = " . "
                    else:
                        print("Try something else")
                        moves()
        else:
            print("Try something else")
            moves()

    else:
        pass


def rook():
    global x; global y; global mx; global my

    if board[y][x] == " R ":
        piece = board[y][x]
        userinput = input("Write where you want to move: ")
        (userinput[0], userinput[-1])
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
                if board[i][x] == " P " or board[i][x] == " R " or board[i][x] == " H " \
                    or board[i][x] == " B " or board[i][x] == " Q " or board[i][x] == " K ":
                    if not li == y:
                        board[li][x] = piece
                        board[y][x] = " . "
                        break
                    else:
                        print("Try something else")
                        moves()
                elif board[i][x] == " . ":
                    if i == my:
                        board[i][x] = piece
                        board[y][x] = " . "
                        break
                    else:
                        pass
                else:
                    board[i][x] = piece
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
                if board[y][i] == " P " or board[y][i] == " R " or board[y][i] == " H " \
                    or board[y][i] == " B " or board[y][i] == " Q " or board[y][i] == " K ":
                    if not li == x:
                        board[y][li] = piece
                        board[y][x] = " . "
                        break
                    else:
                        print("Try something else")
                        moves()
                elif board[y][i] == " . ":
                    if i == mx:
                        board[y][i] = piece
                        board[y][x] = " . "
                        break
                    else:
                        pass
                else:
                    board[y][i] = piece
                    board[y][x] = " . "
                    break
                li = i
    else:
        pass


def horse():    # Knight
    global x; global y; global mx; global my

    if board[y][x] == " H ":
        piece = board[y][x]
        userinput = input("Write where you want to move: ")
        move(userinput[0], userinput[-1])
        if y < my:
            if y + 1 == my:
                 if x + 2 == mx and board[my][mx] != " P " and board[my][mx] != " R " and board[my][mx] != " H " \
                    and board[my][mx] != " B " and board[my][mx] != " Q " and board[my][mx] != " K ":
                     board[y][x] = " . "
                     board[my][mx] = piece

                 elif x - 2 == mx and board[my][mx] != " P " and board[my][mx] != " R " and board[my][mx] != " H " \
                    and board[my][mx] != " B " and board[my][mx] != " Q " and board[my][mx] != " K ":
                     board[y][x] = " . "
                     board[my][mx] = piece
                 else:
                     print("Try something else")
                     moves()

            elif y + 2 == my:
                if x + 1 == mx and board[my][mx] != " P " and board[my][mx] != " R " and board[my][mx] != " H " \
                     and board[my][mx] != " B " and board[my][mx] != " Q " and board[my][mx] != " K ":
                    board[y][x] = " . "
                    board[my][mx] = piece

                elif x - 1 == mx and board[my][mx] != " P " and board[my][mx] != " R " and board[my][mx] != " H " \
                    and board[my][mx] != " B " and board[my][mx] != " Q " and board[my][mx] != " K ":
                    board[y][x] = " . "
                    board[my][mx] = piece
                else:
                    print("Try something else")
                    moves()
        elif y > my:
            if y - 1 == my:
                if x + 2 == mx and board[my][mx] != " P " and board[my][mx] != " R " and board[my][mx] != " H " \
                        and board[my][mx] != " B " and board[my][mx] != " Q " and board[my][mx] != " K ":
                    board[y][x] = " . "
                    board[my][mx] = piece

                elif x - 2 == mx and board[my][mx] != " P " and board[my][mx] != " R " and board[my][mx] != " H " \
                        and board[my][mx] != " B " and board[my][mx] != " Q " and board[my][mx] != " K ":
                    board[y][x] = " . "
                    board[my][mx] = piece
                else:
                    print("Try something else")
                    moves()
            elif y - 2 == my:
                if x + 1 == mx and board[my][mx] != " P " and board[my][mx] != " R " and board[my][mx] != " H " \
                     and board[my][mx] != " B " and board[my][mx] != " Q " and board[my][mx] != " K ":
                    board[y][x] = " . "
                    board[my][mx] = piece

                elif x - 1 == mx and board[my][mx] != " P " and board[my][mx] != " R " and board[my][mx] != " H " \
                    and board[my][mx] != " B " and board[my][mx] != " Q " and board[my][mx] != " K ":
                    board[y][x] = " . "
                    board[my][mx] = piece
                else:
                    print("Try something else")
                    moves()

    else:
        pass


def bishop(): # THIS IS TERRIBLE CODE, FIX IT LATER
    global x; global y; global mx; global my

    if board[y][x] == " B ":
        piece = board[y][x]
        userinput = input("Write where you want to move: ")
        move(userinput[0], userinput[-1])
        ay = y
        ax = x
        if y > my:
            if x > mx:
                while True:
                    ay -= 1
                    ax -= 1
                    if board[ay][ax] == " P " or board[ay][ax] == " R " or board[ay][ax] == " H " \
                            or board[ay][ax] == " B " or board[ay][ax] == " Q " or board[ay][ax] == " K ":
                        mx = ax + 1
                        my = ay + 1
                        board[my][mx] = piece
                        board[y][x] = " . "
                        break
                    elif not board[ay][ax] == " P " or board[ay][ax] == " R " or board[ay][ax] == " H " \
                            or board[ay][ax] == " B " or board[ay][ax] == " Q " or board[ay][ax] == " K ":
                        if ay == my and ax == mx:
                            board[my][mx] = piece
                            board[y][x] = " . "
                            break
                        elif not board[ay][ax] == " . ":
                            board[ay][ax] = piece
                            board[y][x] = " . "
                            break
                    else:
                        print("Try something else")
                        moves()
            elif x < mx:
                while True:
                    ay -= 1
                    ax += 1
                    if board[ay][ax] == " P " or board[ay][ax] == " R " or board[ay][ax] == " H " \
                        or board[ay][ax] == " B " or board[ay][ax] == " Q " or board[ay][ax] == " K ":
                        mx = ax - 1
                        my = ay + 1
                        board[my][mx] = piece
                        board[y][x] = " . "
                        break
                    elif not board[ay][ax] == " P " or board[ay][ax] == " R " or board[ay][ax] == " H " \
                        or board[ay][ax] == " B " or board[ay][ax] == " Q " or board[ay][ax] == " K ":
                        if ay == my and ax == mx:
                            board[my][mx] = piece
                            board[y][x] = " . "
                            break
                        elif not board[ay][ax] == " . ":
                            board[ay][ax] = piece
                            board[y][x] = " . "
                            break
                    else:
                        print("Try something else")
                        moves()
            else:
                print("Try something else")
                moves()
        elif y < my:
            if x > mx:
                while True:
                    ay += 1
                    ax -= 1
                    if board[ay][ax] == " P " or board[ay][ax] == " R " or board[ay][ax] == " H " \
                            or board[ay][ax] == " B " or board[ay][ax] == " Q " or board[ay][ax] == " K ":
                        mx = ax + 1
                        my = ay - 1
                        board[my][mx] = piece
                        board[y][x] = " . "
                        break
                    elif not board[ay][ax] == " P " or board[ay][ax] == " R " or board[ay][ax] == " H " \
                            or board[ay][ax] == " B " or board[ay][ax] == " Q " or board[ay][ax] == " K ":
                        if ay == my and ax == mx:
                            board[my][mx] = piece
                            board[y][x] = " . "
                            break
                        elif not board[ay][ax] == " . ":
                            board[ay][ax] = piece
                            board[y][x] = " . "
                            break
                    else:
                        print("Try something else")
                        moves()
            elif x < mx:
                while True:
                    ay += 1
                    ax += 1
                    if board[ay][ax] == " P " or board[ay][ax] == " R " or board[ay][ax] == " H " \
                            or board[ay][ax] == " B " or board[ay][ax] == " Q " or board[ay][ax] == " K ":
                        mx = ax - 1
                        my = ay - 1
                        board[my][mx] = piece
                        board[y][x] = " . "
                        break
                    elif not board[ay][ax] == " P " or board[ay][ax] == " R " or board[ay][ax] == " H " \
                            or board[ay][ax] == " B " or board[ay][ax] == " Q " or board[ay][ax] == " K ":
                        if ay == my and ax == mx:
                            board[my][mx] = piece
                            board[y][x] = " . "
                            break
                        elif not board[ay][ax] == " . ":
                            board[ay][ax] = piece
                            board[y][x] = " . "
                            break
                    else:
                        print("Try something else")
                        moves()
            else:
                print("Try something else")
                moves()

        else:
            print("Try something else")
            moves()

    else:
        pass


def queen():    # It's just bishop and rook
    global x; global y; global mx; global my

    if board[y][x] == " Q ":
        piece = board[y][x]
        userinput = input("Write where you want to move: ")
        move(userinput[0], userinput[-1])
        ay = y
        ax = x
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
                if board[i][x] == " P " or board[i][x] == " R " or board[i][x] == " H " \
                        or board[i][x] == " B " or board[i][x] == " Q " or board[i][x] == " K ":
                    if not li == y:
                        board[li][x] = piece
                        board[y][x] = " . "
                        break
                    else:
                        print("Try something else")
                        moves()
                elif board[i][x] == " . ":
                    if i == my:
                        board[i][x] = piece
                        board[y][x] = " . "
                        break
                    else:
                        pass
                else:
                    board[i][x] = piece
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
                if board[y][i] == " P " or board[y][i] == " R " or board[y][i] == " H " \
                        or board[y][i] == " B " or board[y][i] == " Q " or board[y][i] == " K ":
                    if not li == x:
                        board[y][li] = piece
                        board[y][x] = " . "
                        break
                    else:
                        print("Try something else")
                        moves()
                elif board[y][i] == " . ":
                    if i == mx:
                        board[y][i] = piece
                        board[y][x] = " . "
                        break
                    else:
                        pass
                else:
                    board[y][i] = piece
                    board[y][x] = " . "
                    break
                li = i
        elif y > my:
            if x > mx:
                while True:
                    ay -= 1
                    ax -= 1
                    if board[ay][ax] == " P " or board[ay][ax] == " R " or board[ay][ax] == " H " \
                            or board[ay][ax] == " B " or board[ay][ax] == " Q " or board[ay][ax] == " K ":
                        mx = ax + 1
                        my = ay + 1
                        board[my][mx] = piece
                        board[y][x] = " . "
                        break
                    elif not board[ay][ax] == " P " or board[ay][ax] == " R " or board[ay][ax] == " H " \
                            or board[ay][ax] == " B " or board[ay][ax] == " Q " or board[ay][ax] == " K ":
                        if ay == my and ax == mx:
                            board[my][mx] = piece
                            board[y][x] = " . "
                            break
                        elif not board[ay][ax] == " . ":
                            board[ay][ax] = piece
                            board[y][x] = " . "
                            break
                    else:
                        print("Try something else")
                        moves()
            elif x < mx:
                while True:
                    ay -= 1
                    ax += 1
                    if board[ay][ax] == " P " or board[ay][ax] == " R " or board[ay][ax] == " H " \
                        or board[ay][ax] == " B " or board[ay][ax] == " Q " or board[ay][ax] == " K ":
                        mx = ax - 1
                        my = ay + 1
                        board[my][mx] = piece
                        board[y][x] = " . "
                        break
                    elif not board[ay][ax] == " P " or board[ay][ax] == " R " or board[ay][ax] == " H " \
                        or board[ay][ax] == " B " or board[ay][ax] == " Q " or board[ay][ax] == " K ":
                        if ay == my and ax == mx:
                            board[my][mx] = piece
                            board[y][x] = " . "
                            break
                        elif not board[ay][ax] == " . ":
                            board[ay][ax] = piece
                            board[y][x] = " . "
                            break
                    else:
                        print("Try something else")
                        moves()
            else:
                print("Try something else")
                moves()
        elif y < my:
            if x > mx:
                while True:
                    ay += 1
                    ax -= 1
                    if board[ay][ax] == " P " or board[ay][ax] == " R " or board[ay][ax] == " H " \
                            or board[ay][ax] == " B " or board[ay][ax] == " Q " or board[ay][ax] == " K ":
                        mx = ax + 1
                        my = ay - 1
                        board[my][mx] = piece
                        board[y][x] = " . "
                        break
                    elif not board[ay][ax] == " P " or board[ay][ax] == " R " or board[ay][ax] == " H " \
                            or board[ay][ax] == " B " or board[ay][ax] == " Q " or board[ay][ax] == " K ":
                        if ay == my and ax == mx:
                            board[my][mx] = piece
                            board[y][x] = " . "
                            break
                        elif not board[ay][ax] == " . ":
                            board[ay][ax] = piece
                            board[y][x] = " . "
                            break
                    else:
                        print("Try something else")
                        moves()
            elif x < mx:
                while True:
                    ay += 1
                    ax += 1
                    if board[ay][ax] == " P " or board[ay][ax] == " R " or board[ay][ax] == " H " \
                            or board[ay][ax] == " B " or board[ay][ax] == " Q " or board[ay][ax] == " K ":
                        mx = ax - 1
                        my = ay - 1
                        board[my][mx] = piece
                        board[y][x] = " . "
                        break
                    elif not board[ay][ax] == " P " or board[ay][ax] == " R " or board[ay][ax] == " H " \
                            or board[ay][ax] == " B " or board[ay][ax] == " Q " or board[ay][ax] == " K ":
                        if ay == my and ax == mx:
                            board[my][mx] = piece
                            board[y][x] = " . "
                            break
                        elif not board[ay][ax] == " . ":
                            board[ay][ax] = piece
                            board[y][x] = " . "
                            break
                    else:
                        print("Try something else")
                        moves()
            else:
                print("Try something else")
                moves()

        else:
            print("Try something else")
            moves()

    else:
        pass


def king():
    global x; global y; global mx; global my; global check; global check2; global check3; global check4; global check5; global check52

    if board[y][x] == " K ":
        piece = board[y][x]
        userinput = input("Write where you want to move: ")
        move(userinput[0], userinput[-1])
        if x == mx and board[my][mx] != " P " and board[my][mx] != " R " and board[my][mx] != " H " \
                            and board[my][mx] != " B " and board[my][mx] != " Q " and board[my][mx] != " K ":

            if y + 1 == my or y - 1 == my:
                board[y][x] = " . "
                s = board[my][mx]
                board[my][mx] = piece
                kingcheck()
                if check == 1 or check2 == 1 or check3 == 1 or check4 == 1 or check5 == 1 or check52 == 1:
                    print("You can't move there")
                    board[y][x] = piece
                    board[my][mx] = s
                    check, check2, check3, check4, check5, check52 = 0, 0, 0, 0, 0, 0
                    moves()
            else:
                print("You can't move there, try sth else")
                moves()
        elif y == my and board[my][mx] != " P " and board[my][mx] != " R " and board[my][mx] != " H " \
                            and board[my][mx] != " B " and board[my][mx] != " Q " and board[my][mx] != " K ":
            if x + 1 == my or x - 1 == my:
                board[y][x] = " . "
                s = board[my][mx]
                board[my][mx] = piece
                kingcheck()
                if check == 1 or check2 == 1 or check3 == 1 or check4 == 1 or check5 == 1 or check52 == 1:
                    print("You can't move there")
                    board[y][x] = piece
                    board[my][mx] = s
                    check, check2, check3, check4, check5, check52 = 0, 0, 0, 0, 0, 0
                    moves()
            else:
                print("You can't move there, try sth else")
                moves()
        elif x + 1 == mx and board[my][mx] != " P " and board[my][mx] != " R " and board[my][mx] != " H " \
                            and board[my][mx] != " B " and board[my][mx] != " Q " and board[my][mx] != " K ":
            if y + 1 == my or y - 1 == my:
                board[y][x] = " . "
                s = board[my][mx]
                board[my][mx] = piece
                kingcheck()
                if check == 1 or check2 == 1 or check3 == 1 or check4 == 1 or check5 == 1 or check52 == 1:
                    print("You can't move there")
                    board[y][x] = piece
                    board[my][mx] = s
                    check, check2, check3, check4, check5, check52 = 0, 0, 0, 0, 0, 0
                    moves()
            else:
                print("You can't move there, try sth else")
                moves()
        elif x - 1 == mx and board[my][mx] != " P " and board[my][mx] != " R " and board[my][mx] != " H " \
                            and board[my][mx] != " B " and board[my][mx] != " Q " and board[my][mx] != " K ":
            if y + 1 == my or y - 1 == my:
                board[y][x] = " . "
                s = board[my][mx]
                board[my][mx] = piece
                kingcheck()
                if check == 1 or check2 == 1 or check3 == 1 or check4 == 1 or check5 == 1 or check52 == 1:
                    print("You can't move there")
                    board[y][x] = piece
                    board[my][mx] = s
                    check, check2, check3, check4, check5, check52 = 0, 0, 0, 0, 0, 0
                    moves()
            else:
                print("You can't move there, try sth else")
                moves()
        else:
            print("You can't move there, try sth else")
            moves()

    else:
        pass

def checkifdot():
    global x
    global y
    if board[y][x] == " . ":
        print("Try something else")
        moves()
    else:
        pass