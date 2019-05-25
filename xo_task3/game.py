from board import Board
from btree import Tree

cells = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0),
         5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}

class Game:
    def __init__(self):
        sign = input('> If you want to play for a X - press X, else print 0 :')
        print('___________________________________________________________')
        print('WELCOME TO THE TIC.TOC.TOE GAME!')
        print('THIS IS A STARTING EMPTY BOARD!')
        if sign == 'X' or sign == 'x':
            self.player = 1
            self.board = Board(True)
        elif sign == 'O' or sign == '0':
            self.player = -1
            self.board = Board(False)
        self.tree = Tree(self.board)

    def game(self):
        self.tree.root.board.draw()
        if self.player == 1:
            print('YOUR TURN!')
            move_cell = int(input('>>> Enter a number of cell from 1 to 9 : '))
            cell = cells[move_cell]
            while not self.tree.root.board.check_user_move(cell):
                move_cell = int(input('>>> Enter a number of cell from 1 to 9 : '))
                cell = cells[move_cell]
            self.tree = self.tree.move(cell)
        else:
            print('Computer is choosing his move...')
            cell = self.tree.search_best_move()
            self.tree = self.tree.move(cell)

        current_state = self.tree.root.board.has_winner()
        if current_state == 2:  # no winner
            self.tree.root.board.draw()
            print('That`s a draw')
            return False
        elif current_state == 1:
            self.tree.root.board.draw()
            print('You loose')
            return False
        elif current_state == -1:
            self.tree.root.board.draw()
            print('You win')
            return False
        self.player = -self.player
        return True

    def play(self):
        fl = True
        while fl:
            fl = self.game()


if __name__ == '__main__':
    Game().play()
