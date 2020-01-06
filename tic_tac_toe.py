from random import choice


class TicTacToe:
    def __init__(self):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.available_moves = {1: (0, 0),
                                2: (0, 1),
                                3: (0, 2),
                                4: (1, 0),
                                5: (1, 1),
                                6: (1, 2),
                                7: (2, 0),
                                8: (2, 1),
                                9: (2, 2)
                                }
        self.computer = "x"
        self.user = "o"
        self.difficulty = "easy"
        self.mode = "single"
        self.score_user01 = 0
        self.score_user02 = 0
        self.score_computer = 0

    def choose_difficulty(self, choice: str):
        if choice != "easy" and choice != "medium" and choice != "hard":  # checks if choice is valid, if not return 0
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
        if self.board[int(row)][int(column)] == 0:  # if chosen position is valid, return 1
            return 1
        return 0

    def move_key(self, pos: tuple):
        if pos == (0, 0):
            return 1
        elif pos == (0, 1):
            return 2
        elif pos == (0, 2):
            return 3
        elif pos == (1, 0):
            return 4
        elif pos == (1, 1):
            return 5
        elif pos == (1, 2):
            return 6
        elif pos == (2, 0):
            return 7
        elif pos == (2, 1):
            return 8
        elif pos == (2, 2):
            return 9
        return -1

    # easy mode means the computer will play at random
    # hard mode means the computer will run a backtracking algorithm to determine next move
    def next_move(self):
        if self.difficulty == "easy":
            while True:
                current_move = choice(list(self.available_moves))
                # verify if random position chosen is available
                is_valid = self.slot_available(self.available_moves[current_move])

                if is_valid:
                    row, column = self.available_moves[current_move]
                    # self.board[row][column] = self.computer  # changes position value to pc piece
                    # self.available_moves.pop(current_move)
                    # both statements are unnecessary as it will be done in GUI Level once function is called
                    # this is only used when debugging the class directly thru play_game()

                    return row, column

                    break
        elif self.difficulty == "medium":
            pass
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

    # Verifies if game has tied
    # returns 0 if game has NOT tied
    # returns 1 if game has tied
    def has_tied(self):
        for row in self.board:
            if 0 in row:
                return 0
        return 1

    # Resets "all" control variables or "part" of control variables
    # All: used to fully reset the game, restart
    # Part: used to clear board an piece options, but score ramains
    def reset(self, option: str):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.available_moves = {1: (0, 0),
                                2: (0, 1),
                                3: (0, 2),
                                4: (1, 0),
                                5: (1, 1),
                                6: (1, 2),
                                7: (2, 0),
                                8: (2, 1),
                                9: (2, 2)
                                }
        if option == "all":
            self.computer = "x"
            self.user = "o"
            self.mode = "single"
            self.score_user01 = 0
            self.score_user02 = 0
            self.score_computer = 0

    # rough print used to debug game logic
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
        if self.choose_difficulty(difficulty):
            # 2
            piece = input("Choose your piece: ").lower()
            if self.choose_pieces(piece):
                # 3
                if self.user == "x":
                    while True:
                        self.print_board()
                        # 3.1
                        move = input("Choose your position (row,column): ")
                        row, column = move.split(",")
                        row = int(row)
                        column = int(column)
                        # add a try except here
                        if self.slot_available((row, column)):
                            self.board[row][column] = self.user
                            my_move = self.move_key((row, column))
                            if my_move == -1:
                                break
                                print("here")
                            else:
                                self.available_moves.pop(my_move)

                            game_ended = self.has_won()
                            if game_ended[0] == 1:
                                print(f"{game_ended[1].upper()} has won!")
                                break
                            if self.has_tied():
                                print("Game tied!")
                                break
                            # 3.2
                            self.next_move()
                            if self.has_tied():
                                print("Game tied!")
                                break
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

                        if self.has_tied():
                            print("Game tied!")
                            break
                        game_ended = self.has_won()
                        if game_ended[0] == 1:
                            print(f"{game_ended[1].upper()} has won!")
                            break

                        # 3.1
                        while True:
                            move = input("Choose your position (row,column): ")
                            row, column = move.split(",")

                            if self.slot_available((row, column)):
                                self.board[int(row)][int(column)] = self.user
                                my_move = self.move_key((row, column))
                                if my_move == -1:
                                    break
                                else:
                                    self.available_moves.pop(my_move)
                                if self.has_tied():
                                    print("Game tied!")
                                    break
                                # 4
                                game_ended = self.has_won()
                                if game_ended[0] == 1:
                                    print(f"{game_ended[1].upper()} has won!")
                                    break
                            else:
                                print("Position already taken! Choose another one.")

                        # 5
                        self.print_board()


# my_board = TicTacToe()
# my_board.play_game()
