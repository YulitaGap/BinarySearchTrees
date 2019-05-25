from board import Board
from btree import Tree

cells = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0),
         5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1),
         9: (2, 2)}


class GameLogic:

    def __init__(self):
        """
        Initialization of TicTocToe GameLogic class.
        """
        print('___________________________________________________________')
        print('WELCOME TO THE TIC.TOC.TOE GAME!')
        print('THIS IS A STARTING EMPTY BOARD!')
        self.board = None
        while not self.board:
            sign = input('> If you want to play for a X - press X, else print 0 :')
            if sign == 'X' or sign == 'x':
                self.player = 1
                self.board = Board(True)
            elif sign == 'O' or sign == '0' or sign == 'o':
                self.player = -1
                self.board = Board(False)
        self.tree = Tree(self.board)

    def game(self):
        self.tree.root.board.draw()
        self.play = True
        while self.play:
            if self.player == 1:
                print('YOUR TURN!')
                try:
                    move_cell = int(input('>>> Enter a number of cell from 1 to 9 : '))
                    cell = cells[move_cell]
                except KeyError:
                    move_cell = int(input('>>> Enter a number of cell from 1 to 9 : '))
                    cell = cells[move_cell]
                while not self.tree.root.board.check_user_move(cell):
                    move_cell = int(input('>>> Enter a number of cell from 1 to 9 : '))
                    cell = cells[move_cell]
                self.tree = self.tree.move(cell)
            else:
                print("BOT's TURN!")
                cell = self.tree.choose_optimal_way()
                self.tree = self.tree.move(cell)

            current_state = self.tree.root.board.has_winner()
            if current_state == 2:  # no winner
                self.tree.root.board.draw()
                self.play = False

            elif current_state == -1:
                self.tree.root.board.draw()
                print('YOU WIN!')
                self.play = False
                break

            elif current_state == 1:
                self.tree.root.board.draw()
                print('COMPUTER WIN!')
                self.play = False
                break

            self.player = -self.player
            self.play = True


if __name__ == '__main__':
    GameLogic().game()
