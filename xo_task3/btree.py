from btnode import Node
from random import shuffle

class Tree:
    """
    Class for Tree representation
    """
    def __init__(self, board, cell=None):
        self.root = Node(board, cell)
        self.states = []

    def clear(self):
        self.root = None
    
    def move(self, where):
        new_board = self.root.move(where)
        new_tree = Tree(new_board)
        new_tree.root.cell = None
        return new_tree
