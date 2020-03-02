###############################################
# ---------------------------------------------#
###############################################
# Model planszy z BoarDict.py
# Powód przeniesienia: Plansza stworzona na podstawie listy jest prostrza i łatwiejsza
# w użyciu niż ta na podstawie słownika.

board = {3.3:" . ", 3.2: " . ", 3.1: " . ", 2.3: " . ", 2.2: " . ", 2.1: " . ", 1.3: " . ", 1.2: " p ", 1.1: " . "}

def printboard():
    print("3" + board[3.3] + board[3.2] + board[3.1] + "\n"
          "2" + board[2.3] + board[2.2] + board[2.1] + "\n"
          "1" + board[1.3] + board[1.2] + board[1.1] + "\n"
          " " + " a " + " b " + " c ")
printboard()

if input() == a1:

###############################################
# ---------------------------------------------#
###############################################
# Wieża 1.1 z Figury.py
# Powód przeniesienia: da się to zrobić prościej, nie działa poprawnie


def rook():
    global x
    global y
    if board[y][x] == " r ":
        userinput = input("Where you want to move: ")
        move(userinput[0], userinput[-1])
        if x == mx:
            if y > my:
                rookmvyw()
            else:
                rookmvys()

        elif x != mx:
            if x > mx:
                rookmvxd()
            else:
                rookmvxa()

        boardprint()
    else:
        pass


def rookmvyw():
    for i in range(7, -1, -1):
        if not board[i][x] == " . ":
            if board[i][x] == " p " or board[i][x] == " r " or board[i][x] == " h " \
                    or board[i][x] == " b " or board[i][x] == " q " or board[i][x] == " k ":
                if i != y:
                    i += 1
                    if i == y:
                        print("Try something else")
                        rook()
                    else:
                        board[y][x] = " . "
                        board[i][x] = " r "
                        break
            else:
                board[y][x] = " . "
                board[i][x] = " r "
                break
        else:
            if i == my:
                board[y][x] = " . "
                board[i][x] = " r "
                break


def rookmvys():
    for i in range(0, 8):
        if not board[i][x] == " . ":
            if board[i][x] == " p " or board[i][x] == " r " or board[i][x] == " h " \
                    or board[i][x] == " b " or board[i][x] == " q " or board[i][x] == " k ":
                if i != y:
                    i += 1
                    if i == y:
                        print("Try something else")
                        rook()
                    else:
                        board[y][x] = " . "
                        board[i][x] = " r "
                        break
            else:
                board[y][x] = " . "
                board[i][x] = " r "
                break
        else:
            if i == my:
                board[y][x] = " . "
                board[i][x] = " r "
                break


def rookmvxa():
    for i in range(7, -1, -1):
        if not board[y][i] == " . ":
            if board[y][i] == " p " or board[y][i] == " r " or board[y][i] == " h " \
                    or board[y][i] == " b " or board[y][i] == " q " or board[y][i] == " k ":
                if i != x and i > 0:
                    i -= 1
                    if i == x:
                        print("Try something else")
                        rook()
                    else:
                        board[y][x] = " . "
                        board[y][i] = " r "
                        break
                elif i != x and i < 7:
                    i += 1
                    if i == x:
                        print("Try something else")
                        rook()
                    else:
                        board[y][x] = " . "
                        board[y][i] = " r "
            else:
                board[y][x] = " . "
                board[y][i] = " r "
                break
        else:
            if i == mx:
                board[y][x] = " . "
                board[y][i] = " r "
                break


def rookmvxd():
    for i in range(0, 8):
        if not board[y][i] == " . ":
            if board[y][i] == " p " or board[y][i] == " r " or board[y][i] == " h " \
                    or board[y][i] == " b " or board[y][i] == " q " or board[y][i] == " k ":
                if i != x and i > 0:
                    i -= 1
                    if i == x:
                        print("Try something else")
                        rook()
                    else:
                        board[y][x] = " . "
                        board[y][i] = " r "
                        break
                elif i != x and i < 7:
                    i += 1
                    if i == x:
                        print("Try something else")
                        rook()
                    else:
                        board[y][x] = " . "
                        board[y][i] = " r "
            else:
                board[y][x] = " . "
                board[y][i] = " r "
                break
        else:
            if i == mx:
                board[y][x] = " . "
                board[y][i] = " r "
                break


###############################################
# ---------------------------------------------#
###############################################
# Pion 1.0 z Figury.py
# Powód przeniesienia: zmiana modelu sterowania.

def pawn():
    global x
    global y
    if board[y][x] == " p ":
        userinput = input("Where you want to move: ")
        if userinput == "w":
            if y > 0:
                y -= 1
                if board[y][x] == " . ":
                    board[y][x] = " p "
                    y += 1
                    board[y][x] = " . "
                    boardprint()
                else:
                    pawn()
            else:
                pawn()
        elif userinput == "wd":
            if y > 0 and x < 2:
                y -= 1
                x += 1
                if not board[y][x] == " . ":
                    board[y][x] = " p "
                    y += 1
                    x -= 1
                    board[y][x] = " . "
                    boardprint()
                else:
                    pawn()
            else:
                pawn()

        elif userinput == "wa":
            if x > 0 and y < 2:
                x -= 1
                y -= 1
                if not board[y][x] == " . ":
                    board[y][x] = " p "
                    x += 1
                    y += 1
                    board[y][x] = " . "
                    boardprint()
                else:
                    y += 1
                    x += 1
                    print("Try something else")
                    pawn()
            else:
                pawn()

    else:
        pass

###############################################
# ---------------------------------------------#
###############################################
