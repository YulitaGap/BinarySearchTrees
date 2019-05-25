from btnode import Node
import random


class Tree:
    """
    Class for Tree representation.
    """
    def __init__(self, board, cell=None):
        self.root = Node(board, cell)
        self.states = []

    def clear(self):
        """
        Clear all nodes of Tree.
        """
        self.root = None

    def form_tree(self):
        """
        Build a tree of all possible moves in game.
        :return: None
        """
        possible_cells = self.root.board.possible_moves()
        random.shuffle(possible_cells)
        for cell in possible_cells:
            renewed_board = self.root.move(cell)
            renewed_tree = Tree(renewed_board, cell)
            renewed_tree.form_tree()
            self.states.append(renewed_tree)
        return

    def count_state(self):
        """
        Count values of tree branches for choosing best move.
        :return: int
        """
        curr_state = self.root.board.has_winner()
        if curr_state != self.root.board.NOT_FINISHED and curr_state != self.root.board.DRAW:
            self.root.result = curr_state
        else:
            way_value = []
            for state in self.states:
                state.count_state()
                way_value.append(state.root.result)
            if self.root.board.last_move == self.root.board.CROSS:
                self.root.result = max(way_value)
            else:
                self.root.result = min(way_value)

    def choose_optimal_way(self, optimal=None):
        """
        Choosing best move on board on counted way values.
        :param optimal: subtree
        :return: tuple
        """
        self.form_tree()
        self.count_state()
        for state in self.states:
            if self.root.result < state.root.result or (
                    state.root.result == self.root.result and (not optimal or len(state) > len(optimal))):
                optimal = state
        return optimal.root.cell

    def __iter__(self):
        """
        Iteration process realization.
        """
        return self.states.__iter__()

    def __len__(self):
        """
        Counting length by recursion realization.
        """
        def recurse(tree):
            if tree.states is False:
                return 0
            else:
                return max([recurse(elem) for elem in tree.games]) + 1

        return recurse(self)

    def move(self, move_cell):
        """
        Returns a tree after  move to inputted cell.
        :param move_cell: tuple
        :return: Tree
        """
        renewed_board = self.root.move(move_cell)
        renewed_tree = Tree(renewed_board)
        renewed_tree.root.cell = None
        return renewed_tree 
