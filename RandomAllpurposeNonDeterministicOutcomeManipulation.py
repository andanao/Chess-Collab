import chess
import math
# done 10:12
# moveset = ["d2d4", "e1c3", "c1f4", "c3c7"]

class engine:
    # needs initializer
    def __init__(self):
        pass
    
    def play(self, board, tlim):
        legalmoves = board.legal_moves
        random_num = random()%len(legalmoves)
        optimal_play = chess.Move.from_uci(legalmoves[random_num])
        return optimal_play
