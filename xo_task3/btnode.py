class Node:
    """
    Class for Tree Node representation
    """
    def __init__(self, board, cell=None, result=0):
        self.board = board
        self.cell = cell
        self.result = result

    def move(self, move_cell):
        return self.board.move(move_cell)

    def check_state(self):
        return self.board.has_winner() 
