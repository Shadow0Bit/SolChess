R, H, B, Q, K, B2, H2, R2 = " R ", " H ", " B ", " Q ", " K ", " B ", " H ", " R "
P1, P2, P3, P4, P5, P6, P7, P8 = " P ", " P ", " P ", " P ", " P ", " P ", " P ", " P "
r, h, b, q, k, b2, h2, r2 = " r ", " h ", " b ", " q ", " k ", " b ", " h ", " r "
p1, p2, p3, p4, p5, p6, p7, p8 = " p ", " p ", " p ", " p ", " p ", " p ", " p ", " p "

board = [[R, H, B, Q, K, B2, H2, R2],  # 0
         [P1, P2, P3, P4, P5, P6, P7, P8],  # 1
         [" . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "],  # 2
         [" . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "],  # 3
         [" . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "],  # 4
         [" . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "],  # 5
         [p1, p2, p3, p4, p5, p6, p7, p8],  # 6
         [r, h, b, q, k, b2, h2, r2]]  # 7


def boardprint():
    print(  "8" + board[0][0] + board[0][1] + board[0][2] + board[0][3] + board[0][4] + board[0][5] + board[0][6] + board[0][7] + "\n"
            "7" + board[1][0] + board[1][1] + board[1][2] + board[1][3] + board[1][4] + board[1][5] + board[1][6] + board[1][7] + "\n"
            "6" + board[2][0] + board[2][1] + board[2][2] + board[2][3] + board[2][4] + board[2][5] + board[2][6] + board[2][7] + "\n"
            "5" + board[3][0] + board[3][1] + board[3][2] + board[3][3] + board[3][4] + board[3][5] + board[3][6] + board[3][7] + "\n"
            "4" + board[4][0] + board[4][1] + board[4][2] + board[4][3] + board[4][4] + board[4][5] + board[4][6] + board[4][7] + "\n"
            "3" + board[5][0] + board[5][1] + board[5][2] + board[5][3] + board[5][4] + board[5][5] + board[5][6] + board[5][7] + "\n"
            "2" + board[6][0] + board[6][1] + board[6][2] + board[6][3] + board[6][4] + board[6][5] + board[6][6] + board[6][7] + "\n"
            "1" + board[7][0] + board[7][1] + board[7][2] + board[7][3] + board[7][4] + board[7][5] + board[7][6] + board[7][7] + "\n"
            "  a  b  c  d  e  f  g  h  " + "\n \n")
