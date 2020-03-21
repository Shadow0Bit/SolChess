from Board import board


def black_possible_moves():
    for y in range(0, 8):
        for x in range(0, 8):
            if board[y][x] == " K ":
                king_move = board[y + 1][x]     # str(y+1) + str(x) = yx
                king_move2 = board[y - 1][x]
                king_move3 = board[y][x + 1]
                king_move4 = board[y][x - 1]
                king_move5 = board[y + 1][x + 1]
                king_move6 = board[y + 1][x - 1]
                king_move7 = board[y - 1][x + 1]
                king_move8 = board[y - 1][x - 1]

            if board[y][x] == " Q ":
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
                    queen_move[i] = board[i][ax]

                ax = x
                for i in range(y - 1, -1, -1):
                    ax -= 1
                    if ax == -1:
                        break
                    queen_move2[i] = board[i][ax]

                ax = x
                for i in range(y + 1, 8):
                    ax += 1
                    if ax == 8:
                        break
                    queen_move3[i] = board[i][ax]

                ax = x
                for i in range(y - 1, -1, -1):
                    ax += 1
                    if ax == 8:
                        break
                    queen_move4[i] = board[i][ax]

                for i in range(y - 1, -1, -1):
                    queen_move5[i] = board[i][x]

                for i in range(y + 1, 8):
                    queen_move6[i] = board[i][x]

                for i in range(x - 1, -1, -1):
                    queen_move7[i] = board[y][i]

                for i in range(x + 1, 8):
                    queen_move8[i] = board[y][i]
            if board[y][x] == " B ":
                bishop_move = {}
                bishop_move2 = {}
                bishop_move3 = {}
                bishop_move4 = {}
                ax = x
                for i in range(y + 1, 8):
                    ax -= 1
                    if ax == -1:
                        break
                    bishop_move[i] = board[i][ax]

                ax = x
                for i in range(y - 1, -1, -1):
                    ax -= 1
                    if ax == -1:
                        break
                    bishop_move2[i] = board[i][ax]

                ax = x
                for i in range(y + 1, 8):
                    ax += 1
                    if ax == 8:
                        break
                    bishop_move3[i] = board[i][ax]

                ax = x
                for i in range(y - 1, -1, -1):
                    ax += 1
                    if ax == 8:
                        break
                    bishop_move4[i] = board[i][ax]
            if board[y][x] == " R ":
                rook_move = {}
                rook_move2 = {}
                rook_move3 = {}
                rook_move4 = {}
                for i in range(y - 1, -1, -1):
                    rook_move[i] = board[i][x]

                for i in range(y + 1, 8):
                    rook_move2[i] = board[i][x]

                for i in range(x - 1, -1, -1):
                    rook_move3[i] = board[y][i]

                for i in range(x + 1, 8):
                    rook_move4[i] = board[y][i]

            if board[y][x] == " H ":
                if x < 5 and y < 7:
                    horse_move = board[y + 1][x + 3]
                else: pass