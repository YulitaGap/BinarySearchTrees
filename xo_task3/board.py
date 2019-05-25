from btree import Tree
import random
from copy import deepcopy

# part of code written by O.Dobosevych


def generate_winning_combinations():
    combinations = []
    for i in range(3):
        combination1 = []
        combination2 = []
        for j in range(3):
            combination1.append((i, j))
            combination2.append((j, i))
        combinations.append(combination1)
        combinations.append(combination2)

    combinations.append([(0, 0), (1, 1), (2, 2)])
    combinations.append([(0, 2), (1, 1), (2, 0)])
    return combinations


class Board:
    NOUGHT = 1
    CROSS = -1
    EMPTY = 0
    NOUGHT_WINNER = 1
    CROSS_WINNER = -1
    DRAW = 2
    NOT_FINISHED = 0
    WINNING_COMBINATIONS = generate_winning_combinations()

    def __init__(self, sign=None):
        """
        Initialization of Board class
        :param sign: True / False / None
        """
        self.board = [[0] * 3 for x in range(3)]
        self.last_move = sign
        self.count_moves = 0
        if sign:
            self.last_move = self.NOUGHT
        else:
            self.last_move = self.CROSS

    def draw(self):
        """
        Draws current state of a board
        """
        x = -1
        for i in range(3):
            x += 1
            print('|', end='')
            for j in range(3):
                x +=1
                if self.board[i][j] == 1:
                    print('o', end='|')
                elif self.board[i][j] == -1:
                    print('x', end='|')
                else:
                    if x in range(5, 8):
                        print(x-1, end='|')
                    elif x in range(9, 12):
                        print(x - 2, end='|')
                    else:
                        print(x, end='|')
            print()

    def possible_moves(self):
        """
        Returns all free cells of the board.
        :return: list
        """
        res = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == self.EMPTY:
                    res.append((i, j))
        return res

    def is_full(self):
        """
        Returns true,if there are no free cells,else returns False. 
        """
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    return False
        return True

    def random_move(self):
        """
        Returns random cell for possible move.
        :return: tuple
        """
        board = deepcopy(self)
        tree = Tree(board)

        def recurse(curr_tree):
            possible = curr_tree.root.board.possible_moves()
            if possible:
                rnd_move = random.choice(possible)
                return rnd_move
        return recurse(tree)

    def has_winner(self):
        """
        Returns 2 - if there is no winner, but it's the end of the game.
        Returns 0 - if there is no winner and it's not the end of the game.
        Returns -1/1 - winner signs.
        """
        for combinations in self.WINNING_COMBINATIONS:
            lst = []
            for cell in combinations:
                lst.append(self.board[cell[0]][cell[1]])
            if max(lst) == min(lst) and max(lst) != self.EMPTY:
                return max(lst)
        if self.count_moves == 9 or self.is_full():  # end of the game
            return Board.DRAW

        return self.NOT_FINISHED

    def check_user_move(self, cell):
        """
        Checks if inputted cell is possible for move, raises error if not.
        :param cell: tuple
        :return: bool
        """
        if self.is_full() or self.count_moves == 9:
            return self.DRAW
        if self.board[cell[0]][cell[1]] != self.EMPTY:
            print('Not empty cell,try again!')
            raise IndexError
        return True

    def move(self, move_cell):
        """
        Changes a board according to the move.
        :param move_cell: tuple
        :return: Board
        """
        renewed_board = deepcopy(self)
        renewed_board.last_move = -self.last_move  # changing turn
        renewed_board.board[move_cell[0]][move_cell[1]] = renewed_board.last_move
        renewed_board.count_moves += 1
        return renewed_board

