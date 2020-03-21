import possible_moves as pm
from Board import board

pieces_values = {" k ": 99999, " r ": 5, " h ": 3, " b ": 3, " q ": 9, " p ": 1,
                 " K ": -99999, " R ": -5, " H ": -3, " B ": -3, " Q ": -9, " P ": -1}

pm.black_possible_moves()