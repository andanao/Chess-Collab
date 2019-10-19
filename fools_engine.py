import chess
import chess.engine

# moveset = ["d2d4", "e1c3", "c1f4", "c3c7"]

class fools:
    # needs initializer
    def __init__(self):
        self.moveset = ["d2d4", "e1c3", "c1f4", "c3c7"]
        self.turn = 0
    
    def play(self, board, tlim):
        if self.turn < 4:
            optimal_play = chess.Move.from_uci(self.moveset[self.turn])
        else:
            optimal_play = chess.Move.null()
        self.turn += 1
        print(self.turn)
        return optimal_play
