from Board import board

aiboard = [["R", "H", "B", "Q", "K", "B2", "H2", "R2"],  # 0
         ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"],  # 1
         [".", ".", ".", ".", ".", ".", ".", "."],  # 2
         [".", ".", ".", ".", ".", ".", ".", "."],  # 3
         [".", ".", ".", ".", ".", ".", ".", "."],  # 4
         [".", ".", ".", ".", ".", ".", ".", "."],  # 5
         ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"],  # 6
         ["r", "h", "b", "q", "k2", "b2", "h2", "r2"]]  # 7

def black_possible_moves():
    for y in range(0, 8):
        for x in range(0, 8):
            if aiboard[y][x] == "K":
                king_move = str(y+1) + str(x)
                king_move2 = str(y-1) + str(x)
                king_move3 = str(y) + str(x+1)
                king_move4 = str(y) + str(x-1)
                king_move5 = str(y+1) + str(x+1)
                king_move6 = str(y+1) + str(x-1)
                king_move7 = str(y-1) + str(x+1)
                king_move8 = str(y-1) + str(x-1)
            if aiboard[y][x] == "Q":
                queen_move = {}
                queen_move2 = {}
                queen_move3 = {}
                queen_move4 = {}
                queen_move5 = {}
                queen_move6 = {}
                queen_move7 = {}
                queen_move8 = {}
                ax = x
                for i in range(y + 1, 8):
                    ax -= 1
                    if ax == -1:
                        break
                    queen_move[i] = str(i) + str(ax)

                ax = x
                for i in range(y - 1, -1, -1):
                    ax -= 1
                    if ax == -1:
                        break
                    queen_move2[i] = str(i) + str(ax)

                ax = x
                for i in range(y + 1, 8):
                    ax += 1
                    if ax == 8:
                        break
                    queen_move3[i] = str(i) + str(ax)

                ax = x
                for i in range(y - 1, -1, -1):
                    ax += 1
                    if ax == 8:
                        break
                    queen_move4[i] = str(i) + str(ax)

                for i in range(y - 1, -1, -1):
                    queen_move5[i] = str(i) + str(x)

                for i in range(y + 1, 8):
                    queen_move6[i] = str(i) + str(x)

                for i in range(x - 1, -1, -1):
                    queen_move7[i] = str(y) + str(i)

                for i in range(x + 1, 8):
                    queen_move8[i] = str(y) + str(i)

            if aiboard[y][x] == "B":
                bishop_move1 = {}
                bishop_move2 = {}
                bishop_move3 = {}
                bishop_move4 = {}
                ax = x
                for i in range(y + 1, 8):
                    ax -= 1
                    if ax == -1:
                        break
                    bishop_move1[i] = str(i) + str(ax)

                ax = x
                for i in range(y - 1, -1, -1):
                    ax -= 1
                    if ax == -1:
                        break
                    bishop_move2[i] = str(i) + str(ax)

                ax = x
                for i in range(y + 1, 8):
                    ax += 1
                    if ax == 8:
                        break
                    bishop_move3[i] = str(i) + str(ax)

                ax = x
                for i in range(y - 1, -1, -1):
                    ax += 1
                    if ax == 8:
                        break
                    bishop_move4[i] = str(i) + str(ax)
            if aiboard[y][x] == "B2":
                bishop2_move1 = {}
                bishop2_move2 = {}
                bishop2_move3 = {}
                bishop2_move4 = {}
                ax = x
                for i in range(y + 1, 8):
                    ax -= 1
                    if ax == -1:
                        break
                    bishop2_move1[i] = str(i) + str(ax)

                ax = x
                for i in range(y - 1, -1, -1):
                    ax -= 1
                    if ax == -1:
                        break
                    bishop2_move2[i] = str(i) + str(ax)

                ax = x
                for i in range(y + 1, 8):
                    ax += 1
                    if ax == 8:
                        break
                    bishop2_move3[i] = str(i) + str(ax)

                ax = x
                for i in range(y - 1, -1, -1):
                    ax += 1
                    if ax == 8:
                        break
                    bishop2_move4[i] = str(i) + str(ax)
            if aiboard[y][x] == "R":
                rook_move = {}
                rook_move2 = {}
                rook_move3 = {}
                rook_move4 = {}
                for i in range(y - 1, -1, -1):
                    rook_move[i] = str(i) + str(x)

                for i in range(y + 1, 8):
                    rook_move2[i] = str(i) + str(x)

                for i in range(x - 1, -1, -1):
                    rook_move3[i] = str(y) + str(i)

                for i in range(x + 1, 8):
                    rook_move4[i] = str(y) + str(i)
            if aiboard[y][x] == "R2":
                rook2_move = {}
                rook2_move2 = {}
                rook2_move3 = {}
                rook2_move4 = {}
                for i in range(y - 1, -1, -1):
                    rook2_move[i] = str(i) + str(x)

                for i in range(y + 1, 8):
                    rook2_move2[i] = str(i) + str(x)

                for i in range(x - 1, -1, -1):
                    rook2_move3[i] = str(y) + str(i)

                for i in range(x + 1, 8):
                    rook2_move4[i] = str(y) + str(i)

            if aiboard[y][x] == "H":
                if x < 6 and y < 7:
                    horse_move1 = str(y + 1) + str(x + 2)
                if x < 6 and y > 0:
                    horse_move2 = str(y - 1) + str(x + 2)
                if x > 1 and y < 7:
                    horse_move3 = str(y + 1) + str(x - 2)
                if x > 1 and y > 0:
                    horse_move4 = str(y - 1) + str(x - 2)
                if x < 7 and y < 6:
                    horse_move5 = str(y + 2) + str(x + 1)
                if x < 7 and y > 2:
                    horse_move6 = str(y - 2) + str(x + 1)
                if x > 0 and y < 6:
                    horse_move7 = str(y + 2) + str(x - 1)
                if x > 0 and y > 2:
                    horse_move8 = str(y - 2) + str(x - 1)
            if aiboard[y][x] == "H2":
                if x < 6 and y < 7:
                    horse2_move1 = str(y + 1) + str(x + 2)
                if x < 6 and y > 0:
                    horse2_move2 = str(y - 1) + str(x + 2)
                if x > 1 and y < 7:
                    horse2_move3 = str(y + 1) + str(x - 2)
                if x > 1 and y > 0:
                    horse2_move4 = str(y - 1) + str(x - 2)
                if x < 7 and y < 6:
                    horse2_move5 = str(y + 2) + str(x + 1)
                if x < 7 and y > 2:
                    horse2_move6 = str(y - 2) + str(x + 1)
                if x > 0 and y < 6:
                    horse2_move7 = str(y + 2) + str(x - 1)
                if x > 0 and y > 2:
                    horse2_move8 = str(y - 2) + str(x - 1)

            if aiboard[y][x] == "P1":
                pass