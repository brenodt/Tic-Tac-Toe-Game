from random import random


class TicTacToe:
    def __init__(self):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.computer = "x"
        self.user = "o"
        self.difficulty = "easy"
        self.mode = "single"

    def choose_difficulty(self, choice: str):
        if choice != "easy" and choice != "hard":  # checks if choice is valid, otherwise return 0
            return 0
        self.difficulty = choice
        return 1

    def choose_pieces(self, choice: str):
        if choice.lower() != "x" and choice.lower() != "o":  # not a valid choice, returns 0
            return 0
        if choice == "x":  # valid choices return 1, computer is always opposite to user choice
            self.user = choice
            self.computer = "o"
            return 1
        # if reached this, user choice is "o"
        self.user = choice
        self.computer = "x"
        return 1

    def slot_available(self, pos: tuple):
        row, column = pos
        if self.board[row][column] == 0:  # if chosen position is valid, return 1
            return 1
        return 0

    # easy mode means the computer will play at random
    # hard mode means the computer will run a backtracking algorithm to determine next move
    def next_move(self):
        if self.difficulty == "easy":
            while True:
                row = int(random() * 2)  # random integer between 0 and 2
                column = int(random() * 2)
                # verify if random position chosen is available
                is_valid = self.slot_available((row, column))

                if is_valid:
                    # self.board[row][column] = self.computer  # changes position value to pc piece
                    # unecessary as it will be done in GUI Level once function is called
                    return row, column

                    break

        elif self.difficulty == "hard":
            pass

    # to win, three equal pieces need to be at the same row, column or at one of two diagonals
    # returns: tuple(x, y), where x: 1 == won 0 == lost; y: the piece that won
    def has_won(self):
        # checks rows
        for row in self.board:
            if row[0] == row[1] == row[2]:
                if row[0] != 0:  # 0 represents nothing, so eliminate that group
                    return 1, row[0]

        # checks columns
        for column in range(3):
            if self.board[0][column] == self.board[1][column] == self.board[2][column]:
                if self.board[0][column] != 0:  # 0 represents nothing, so eliminate that group
                    return 1, self.board[0][column]

        # checks both diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            if self.board[0][0] != 0:  # 0 represents nothing, so eliminate that group
                return 1, self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
            if self.board[0][2] != 0:  # 0 represents nothing, so eliminate that group
                return 1, self.board[0][2]

        return 0, 0

    def print_board(self):
        for row in range(3):
            print("  ___ ___ ___")
            for column in range(3):
                if self.board[row][column] != 0:
                    print(f" | {self.board[row][column] }", end="")
                else:
                    print(" |  ", end="")
                if column == 2:
                    print(" |")
            if row == 2:
                print("  ___ ___ ___")

    # 1: User Chooses difficulty
    # 2: User Chooses his piece: o | x
    # 3: Game begins, x always goes first
    #  3.1: if user plays, check slot_available() until valid move
    #  3.2: if pc plays, call next_move()
    # 4: Loop Until game ends, call has_won() to determine
    # 5: print board to visualize position
    def play_game(self):
        # 1
        difficulty = input("Choose Difficulty: ").lower()
        self.choose_difficulty(difficulty)
        # 2
        piece = input("Choose your piece: ").lower()
        self.choose_pieces(piece)
        # 3
        if self.user == "x":
            while True:
                self.print_board()
                # 3.1
                move = input("Choose your position (row,column): ")
                row, column = move.split(",")
                # add a try except here
                if self.slot_available((row, column)):
                    self.board[row][column] = self.user
                    # 3.2
                    self.next_move()
                    # 4
                    game_ended = self.has_won()
                    if game_ended[0] == 1:
                        print(f"{game_ended[1].upper()} has won!")
                        break
                    # 5
                    self.print_board()
                else:
                    print("Position already taken! Choose another one.")
        if self.computer == "x":
            while True:
                # 3.2
                self.next_move()
                self.print_board()
                # 3.1
                while True:
                    move = input("Choose your position (row,column): ")
                    row, column = move.split(",")
                    # add a try except here
                    row = int(row)
                    column = int(column)
                    if self.slot_available((row, column)):
                        self.board[row][column] = self.user
                        break
                    else:
                        print("Position already taken! Choose another one.")
                # 4
                game_ended = self.has_won()
                if game_ended[0] == 1:
                    print(f"{game_ended[1].upper()} has won!")
                    break
                # 5
                self.print_board()


# my_board = TicTacToe()
# my_board.play_game()
