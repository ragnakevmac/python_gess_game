# Author: Kevin Ivan Macandog
# Date: 5/30/2020
# Description: This code can be played as a game like Gess.
# For rules of the game Gess, visit: https://www.chessvariants.com/crossover.dir/gess.html
# This game is usually played on a the squares of an 18x18 grid of a Go board using standard Go stones,
# But here, we use 2-dimensional arrays to portray a board and use 'B' and 'W' to represent the stones and '-' to
# represent an empty block. To play, you can use the make_move function by inputting coordinates as parameters.
# For example, game.make_move('e14', 'g14').
# This code contains only one class that contains all the methods for the mechanics of this game
# and contains all the private data members of the board.



class GessGame:
    '''
    This is a class that contains all the methods for the mechanics of this game and contains all the private data
    members of the board.
    The methods contained in this class are:
    an init method
    get_game_state
    update_game_status
    resign_game
    get_column
    get_row
    check_stones
    check_boundary
    check_own_rings
    check_empty_center
    check_directions
    rec_check_if_path_clear
    check_if_path_clear
    check_if_can_capture
    clear_current_piece
    clear_edges
    move_footprint
    make_move
    '''



    def __init__(self):
        '''
        Initializes the board filled with the player's respective stones on their initial positions.
        "B" for the black stones and "W" for the white stones. And '-' for empty.
        The state of the game is initialized as "UNFINISHED".
        The player turn is initialized to 0 (which is even, because black player goes first).
        '''

        self._game_state = "UNFINISHED"

        self._player_turn = 0       # This is incremented each turn. If it's even, it's black player's turn.
                                    # if it is odd, then it's white player's turn.

        self._board = [
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', 'W', '-', 'W', '-', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', '-', 'W', '-', 'W', '-', '-'],
            ['-', 'W', 'W', 'W', '-', 'W', '-', 'W', 'W', 'W', 'W', '-', 'W', '-', 'W', '-', 'W', 'W', 'W', '-'],
            ['-', '-', 'W', '-', 'W', '-', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', '-', 'W', '-', 'W', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', 'W', '-', '-', 'W', '-', '-', 'W', '-', '-', 'W', '-', '-', 'W', '-', '-', 'W', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', 'B', '-', '-', 'B', '-', '-', 'B', '-', '-', 'B', '-', '-', 'B', '-', '-', 'B', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', 'B', '-', 'B', '-', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', '-', 'B', '-', 'B', '-', '-'],
            ['-', 'B', 'B', 'B', '-', 'B', '-', 'B', 'B', 'B', 'B', '-', 'B', '-', 'B', '-', 'B', 'B', 'B', '-'],
            ['-', '-', 'B', '-', 'B', '-', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', '-', 'B', '-', 'B', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
        ]



    def get_game_state(self):
        '''
        Returns the current game state.
        It can be "UNFINISHED", "BLACK_WON", or "WHITE_WON"
        '''

        return self._game_state



    def update_game_status(self):
        '''
        This is a method that is called after a move is made to check if a player has just broken the opponent's
        last ring. If so, announce the winner if the player captures his or her opponent's last ring.
        If the opponent still has at least one intact ring, continue game.
        '''

        if self._player_turn % 2 == 0:  # if it's black player's turn

            for i in range(1, 19):      # if the opponent (white) still has at least one ring intact on the board,
                for j in range(1, 19):  # continue game. If no more, then BLACK_WON
                    if (
                            (self._board[i][j] == '-') and
                            (self._board[i - 1][j] == 'W') and
                            (self._board[i + 1][j] == 'W') and
                            (self._board[i][j + 1] == 'W') and
                            (self._board[i][j - 1] == 'W') and
                            (self._board[i - 1][j + 1] == 'W') and
                            (self._board[i - 1][j - 1] == 'W') and
                            (self._board[i + 1][j + 1] == 'W') and
                            (self._board[i + 1][j - 1] == 'W')
                    ):
                        return True

            self._game_state = "BLACK_WON"
            return self._game_state


        if self._player_turn % 2 == 1:  # if it's white player's turn

            for i in range(1, 19):      # if the opponent (black) still has at least one ring intact on the board,
                for j in range(1, 19):  # continue game. If no more, then WHITE_WON
                    if (
                            (self._board[i][j] == '-') and
                            (self._board[i - 1][j] == 'B') and
                            (self._board[i + 1][j] == 'B') and
                            (self._board[i][j + 1] == 'B') and
                            (self._board[i][j - 1] == 'B') and
                            (self._board[i - 1][j + 1] == 'B') and
                            (self._board[i - 1][j - 1] == 'B') and
                            (self._board[i + 1][j + 1] == 'B') and
                            (self._board[i + 1][j - 1] == 'B')
                    ):
                        return True

            self._game_state = "WHITE_WON"
            return self._game_state



    def resign_game(self):
        '''
        If the player surrenders during his or her turn, the game ends and gives the opponent the win.
        The way this works is that if the player_turn equals an even number, then that means it's currently the
        black player's turn. If he or she decided to surrender on his or her turn, then WHITE_WON.
        The same this goes when player_turn is an odd number, which will be the white player's current turn.
        '''

        if self._player_turn % 2 == 0:      # if it's black player's turn
            self._game_state = "WHITE_WON"

        else:                               # if it's white player's turn
            self._game_state = "BLACK_WON"


        print(self._game_state)
        return self._game_state



    def get_column(self, string):
        '''
        This method breaks down the string coordinates passed as a parameter and is turns it into an integer for the
        columns. The returned integer is then used to match the list indexes of the game board.
        '''

        column_string = 'abcdefghijklmnopqrst'

        return int(column_string.find(string[0]))       # return the index number instead of a letter.



    def get_row(self, string):
        '''
        This method breaks down the string coordinates passed as a parameter and is turns it into an integer for the
        rows. The returned integer is then used to match the list indexes of the game board.
        '''

        return int(20 - int(string[1:]))                # returns the opposite number because it's in the opposite
                                                        # order of the columns of the board.



    def check_stones(self, old_row, old_column):
        '''
        This method checks whether the 3x3 footprint contains any stones of the opposite player.
        If it does, it returns False. If all is cleared, then it returns True.
        The parts are divided to each player's turn, so the player cannot move the opponent's stones at all.
        So if there is any opponent's stone at the footprint being moved, return False. Otherwise, True.
        '''

        if self._player_turn % 2 == 0:    # if it's black player's turn.
                                          # if the 3x3 footprint being moved contains an opponent's stone, return False

            if self._board[old_row][old_column] == 'W':
                return False

            if self._board[old_row - 1][old_column] == 'W':
                return False

            if self._board[old_row + 1][old_column] == 'W':
                return False

            if self._board[old_row][old_column + 1] == 'W':
                return False

            if self._board[old_row][old_column - 1] == 'W':
                return False

            if self._board[old_row - 1][old_column + 1] == 'W':
                return False

            if self._board[old_row - 1][old_column - 1] == 'W':
                return False

            if self._board[old_row + 1][old_column + 1] == 'W':
                return False

            if self._board[old_row + 1][old_column - 1] == 'W':
                return False


        if self._player_turn % 2 == 1:    # if it's white player's turn.
                                          # if the 3x3 footprint being moved contains an opponent's stone, return False

            if self._board[old_row][old_column] == 'B':
                return False

            if self._board[old_row - 1][old_column] == 'B':
                return False

            if self._board[old_row + 1][old_column] == 'B':
                return False

            if self._board[old_row][old_column + 1] == 'B':
                return False

            if self._board[old_row][old_column - 1] == 'B':
                return False

            if self._board[old_row - 1][old_column + 1] == 'B':
                return False

            if self._board[old_row - 1][old_column - 1] == 'B':
                return False

            if self._board[old_row + 1][old_column + 1] == 'B':
                return False

            if self._board[old_row + 1][old_column - 1] == 'B':
                return False


        return True                       # If the footprint being moved doesn't contain any opponent's stone,
                                          # return True.



    def check_boundary(self, old_row, old_column, new_row, new_column):
        '''
        This method is used to check if one of the blocks at the off-boundary edges are being used as a center of a
        footprint when attempting a move, or, when attempting to place a center into one of the blocks at the
        off-boundary edges. So if the center is going to be off of the inner 18x18 board, return False.
        '''

        if (

            old_row == 0 or             # if the current center is being placed at the top row.
            old_row == 19 or            # if the current center is being placed at the bottom row.
            old_column == 0 or          # if the current center is being placed at the left column.
            old_column == 19 or         # if the current center is being placed at the right column.

            new_row == 0 or             # if the new center is being placed at the top row.
            new_row == 19 or            # if the new center is being placed at the bottom row.
            new_column == 0 or          # if the new center is being placed at the left column.
            new_column == 19            # if the new center is being placed at the right column.

        ):

            return False



    def check_own_rings(self):
        '''
        This is the way to see if the player will still have at least one ring intact on the board when attempting a
        move. The way this works is that it checks each and every block of the board. If it finds a player's ring that
        is still intact, then it returns True and the player stays on the game. If it doesn't find any intact rings on
        the board, then either invalidate the move being attempted (because the player might be moving the ring off the
        board), or, announce a winner because someone just took out his or her opponent's last ring.
        '''

        if self._player_turn % 2 == 0:  # if it's black player's turn

            for i in range(1, 19):      # if black player still has at least one ring intact on the board, return True.
                for j in range(1, 19):  # otherwise, return False and invalidate the move.
                    if (
                            (self._board[i][j] == '-') and
                            (self._board[i-1][j] == 'B') and
                            (self._board[i+1][j] == 'B') and
                            (self._board[i][j+1] == 'B') and
                            (self._board[i][j-1] == 'B') and
                            (self._board[i-1][j+1] == 'B') and
                            (self._board[i-1][j-1] == 'B') and
                            (self._board[i+1][j+1] == 'B') and
                            (self._board[i+1][j-1] == 'B')
                    ):
                        return True

            print("Cannot execute move. You'll lose your last ring!")
            return False


        if self._player_turn % 2 == 1:  # if it's white player's turn

            for i in range(1, 19):      # if white player still has at least one ring intact on the board, return True.
                for j in range(1, 19):  # otherwise, return False and invalidate the move.
                    if (
                            (self._board[i][j] == '-') and
                            (self._board[i-1][j] == 'W') and
                            (self._board[i+1][j] == 'W') and
                            (self._board[i][j+1] == 'W') and
                            (self._board[i][j-1] == 'W') and
                            (self._board[i-1][j+1] == 'W') and
                            (self._board[i-1][j-1] == 'W') and
                            (self._board[i+1][j+1] == 'W') and
                            (self._board[i+1][j-1] == 'W')
                    ):
                        return True

            print("Cannot execute move. You'll lose your last ring!")
            return False



    def check_empty_center(self, old_row, old_column):
        '''
        This method takes the current center as a parameter and
        checks if the center of the player's footprint contains a stone or not. As per the rule,
        if the footprint doesn't have any center, then it can only move up to 3 blocks.
        So this method is used for determining the existence of the footprint's center.
        Returns True if it exists, otherwise False.
        '''

        if self._player_turn % 2 == 0:      # if it's black player's turn

            if self._board[old_row][old_column] == '-':     # if the current center has no player's stone
                return True
            else:
                return False

        if self._player_turn % 2 == 1:      # if it's white player's turn

            if self._board[old_row][old_column] == '-':     # if the current center has no player's stone
                return True
            else:
                return False


    def check_directions(self, old_row, old_column, new_row, new_column):
        '''
        This method takes the current and the next positions as parameters.
        This method returns True if a piece can move into a certain direction, otherwise return False.
        As per the rule of the game, the footprint can onlu go to a certain direction if it has a "stone head pointing
        to that direction". For example, if the center of the footprint has a player's stone at the top right,
        then it means that the footprint can move diagonally to north east. So we can know the direction by subtracting
        the new position from the old position and then getting the "vector" that gives us not just distance, but also
        their positive or negative signs to determine their directions. It also has to strictly go diagonally so
        we have to make sure that their x and y distances are equal to yield a straight diagonal in our 20x20 board.
        If the move can go to a certain direction, returns True, otherwise False.
        '''

        horizontal_distance = new_column - old_column                   # gets the "vector" for horizontal distance
        vertical_distance = new_row - old_row                           # gets the "vector" for vertical distance


        ### if it's black player's turn ###

        if self._player_turn % 2 == 0:

            if vertical_distance < 0 and horizontal_distance == 0:      # if trying to go north
                if self._board[old_row-1][old_column] == 'B':
                    return True
                else:
                    return False

            if vertical_distance > 0 and horizontal_distance == 0:      # if trying to go south
                if self._board[old_row+1][old_column] == 'B':
                    return True
                else:
                    return False

            if vertical_distance == 0 and horizontal_distance > 0:      # if trying to go east
                if self._board[old_row][old_column+1] == 'B':
                    return True
                else:
                    return False

            if vertical_distance == 0 and horizontal_distance < 0:      # if trying to go west
                if self._board[old_row][old_column-1] == 'B':
                    return True
                else:
                    return False


            if vertical_distance < 0 and horizontal_distance > 0:      # if trying to go north-east
                if abs(vertical_distance) == abs(horizontal_distance):  # if it's strictly diagonal
                    if self._board[old_row-1][old_column+1] == 'B':
                        return True
                    else:
                        return False
                else:
                    return False

            if vertical_distance < 0 and horizontal_distance < 0:      # if trying to go north-west
                if abs(vertical_distance) == abs(horizontal_distance):  # if it's strictly diagonal
                    if self._board[old_row-1][old_column-1] == 'B':
                        return True
                    else:
                        return False
                else:
                    return False

            if vertical_distance > 0 and horizontal_distance > 0:      # if trying to go south-east
                if abs(vertical_distance) == abs(horizontal_distance):  # if it's strictly diagonal
                    if self._board[old_row+1][old_column+1] == 'B':
                        return True
                    else:
                        return False
                else:
                    return False

            if vertical_distance > 0 and horizontal_distance < 0:      # if trying to go south-west
                if abs(vertical_distance) == abs(horizontal_distance):  # if it's strictly diagonal
                    if self._board[old_row+1][old_column-1] == 'B':
                        return True
                    else:
                        return False
                else:
                    return False

            if vertical_distance == 0 and horizontal_distance == 0:      # if the move will be at the same spot
                return False


        ### if it's white player's turn ###

        if self._player_turn % 2 == 1:

            if vertical_distance < 0 and horizontal_distance == 0:  # if trying to go north
                if self._board[old_row - 1][old_column] == 'W':
                    return True
                else:
                    return False

            if vertical_distance > 0 and horizontal_distance == 0:  # if trying to go south
                if self._board[old_row + 1][old_column] == 'W':
                    return True
                else:
                    return False

            if vertical_distance == 0 and horizontal_distance > 0:  # if trying to go east
                if self._board[old_row][old_column + 1] == 'W':
                    return True
                else:
                    return False

            if vertical_distance == 0 and horizontal_distance < 0:  # if trying to go west
                if self._board[old_row][old_column - 1] == 'W':
                    return True
                else:
                    return False

            if vertical_distance < 0 and horizontal_distance > 0:      # if trying to go north-east
                if abs(vertical_distance) == abs(horizontal_distance):  # if it's strictly diagonal
                    if self._board[old_row-1][old_column+1] == 'W':
                        return True
                    else:
                        return False
                else:
                    return False

            if vertical_distance < 0 and horizontal_distance < 0:      # if trying to go north-west
                if abs(vertical_distance) == abs(horizontal_distance):  # if it's strictly diagonal
                    if self._board[old_row-1][old_column-1] == 'W':
                        return True
                    else:
                        return False
                else:
                    return False

            if vertical_distance > 0 and horizontal_distance > 0:      # if trying to go south-east
                if abs(vertical_distance) == abs(horizontal_distance):  # if it's strictly diagonal
                    if self._board[old_row+1][old_column+1] == 'W':
                        return True
                    else:
                        return False
                else:
                    return False

            if vertical_distance > 0 and horizontal_distance < 0:      # if trying to go south-west
                if abs(vertical_distance) == abs(horizontal_distance):  # if it's strictly diagonal
                    if self._board[old_row+1][old_column-1] == 'W':
                        return True
                    else:
                        return False
                else:
                    return False

            if vertical_distance == 0 and horizontal_distance == 0:      # if the move will be at the same spot
                return False



    def rec_check_if_path_clear(self, old_row, old_column, distance, counter, direction, new_row, new_column):
        '''
        This is a recursive method that takes the parameters for the current and next positions, distance, direction,
        and counter to know when to stop.
        This recursing method checks to see if a path is clear when moving a footprint, so that it doesn't just
        "jump over" or skip  obstacles on its way, which is not a legal move. So the way this will work is that it will
        recurse through each block the piece is about to head to and check if the path contains an obstacle.
        It will keep recursing until either it hits an obstacle or it reaches the distance the player has requested.
        If any parts of the footprint hits an obstacle on the way, then return False, unless the distance given is just
        about right to capture stones.
        '''


        ### This is a base case to stop when the next center lands on an obstacle ###

        if self._board[new_row][new_column] != '-':                         # if the next center is occupied by a stone
            return False


        ### These are the base cases for stopping when the sides of the footprint hit an obstacle on the way ###

        if self._board[old_row - 1][old_column] != '-':                      # the north side
            if counter == distance:  # It means that the path was clear.
                return True          # Can also capture a stone.
            return False

        if self._board[old_row + 1][old_column] != '-':                      # the south side
            if counter == distance:  # It means that the path was clear.
                return True          # Can also capture a stone.
            return False

        if self._board[old_row][old_column + 1] != '-':                      # the east side
            if counter == distance:  # It means that the path was clear.
                return True          # Can also capture a stone.
            return False

        if self._board[old_row][old_column - 1] != '-':                      # the west side
            if counter == distance:  # It means that the path was clear.
                return True          # Can also capture a stone.
            return False

        if self._board[old_row - 1][old_column + 1] != '-':                  # the north-east side
            if counter == distance:  # It means that the path was clear.
                return True          # Can also capture a stone.
            return False

        if self._board[old_row - 1][old_column - 1] != '-':                  # the north-west side
            if counter == distance:  # It means that the path was clear.
                return True          # Can also capture a stone.
            return False

        if self._board[old_row + 1][old_column + 1] != '-':                  # the south-east side
            if counter == distance:  # It means that the path was clear.
                return True          # Can also capture a stone.
            return False

        if self._board[old_row + 1][old_column - 1] != '-':                  # the south-west side
            if counter == distance:  # It means that the path was clear.
                return True          # Can also capture a stone.
            return False


        ### This is a base case to stop checking when everthing was clear up to the new position. ###

        if self._board[new_row][new_column] == '-':
            if counter == distance:
                return True


        ### These are for recursing, based on the direction going, when each block passed is clear. ###

        if direction == "north":
            return self.rec_check_if_path_clear(old_row - 1, old_column, distance, counter + 1, direction,
                                                new_row, new_column)

        if direction == "south":
            return self.rec_check_if_path_clear(old_row + 1, old_column, distance, counter + 1, direction,
                                                new_row, new_column)

        if direction == "east":
            return self.rec_check_if_path_clear(old_row, old_column + 1, distance, counter + 1, direction,
                                                new_row, new_column)

        if direction == "west":
            return self.rec_check_if_path_clear(old_row, old_column - 1, distance, counter + 1, direction,
                                                new_row, new_column)


        if direction == "north_east":
            return self.rec_check_if_path_clear(old_row - 1, old_column + 1, distance, counter + 1, direction,
                                                new_row, new_column)

        if direction == "north_west":
            return self.rec_check_if_path_clear(old_row - 1, old_column - 1, distance, counter + 1, direction,
                                                new_row, new_column)

        if direction == "south_east":
            return self.rec_check_if_path_clear(old_row + 1, old_column + 1, distance, counter + 1, direction,
                                                new_row, new_column)

        if direction == "south_west":
            return self.rec_check_if_path_clear(old_row + 1, old_column - 1, distance, counter + 1, direction,
                                                new_row, new_column)



    def check_if_path_clear(self, old_row, old_column, new_row, new_column):
        '''
        This is a helper function for the recursive funtion: rec_check_if_path_clear.
        It takes the current and the next positions as parameters, then pass them to the recursive funtion to
        give the details of the footprint and the scene at the destination.
        We also calculate the distance needed for our base case here.
        Then we initialize a counter and pass the direction it's supposed to go to.
        '''


        horizontal_distance = new_column - old_column                    # getting the distances
        vertical_distance = new_row - old_row

        diagonal_distance = 0
        if abs(horizontal_distance) == abs(vertical_distance):
            diagonal_distance = abs(horizontal_distance)

                                                                        # here we make an exception to the recursion
                                                                        # because one step can capture any stones.

        if diagonal_distance == 1:                                      # if going only one step diagonally
            return True

        if abs(vertical_distance) == 1 and horizontal_distance == 0:    # if going only one step north or south
            return True

        if vertical_distance == 0 and abs(horizontal_distance) == 1:    # if going only one step south or east
            return True



        distance = diagonal_distance                                    # I made the variable value closer for access
        counter = 0                                                     # initializes counter


        ### Here we list the right recursive functions based on the direction of where our piece is supposed to go ###

        if horizontal_distance == 0 and vertical_distance < 0:          # if trying to go north
            direction = "north"
            return self.rec_check_if_path_clear(old_row, old_column, abs(vertical_distance), counter, direction,
                                                new_row, new_column)

        if horizontal_distance == 0 and vertical_distance > 0:          # if trying to go south
            direction = "south"
            return self.rec_check_if_path_clear(old_row, old_column, abs(vertical_distance), counter, direction,
                                                new_row, new_column)


        if vertical_distance == 0 and horizontal_distance > 0:          # if trying to go east
            direction = "east"
            return self.rec_check_if_path_clear(old_row, old_column, abs(horizontal_distance), counter, direction,
                                                new_row, new_column)

        if vertical_distance == 0 and horizontal_distance < 0:          # if trying to go west
            direction = "west"
            return self.rec_check_if_path_clear(old_row, old_column, abs(horizontal_distance), counter, direction,
                                                new_row, new_column)


        if vertical_distance < 0 and horizontal_distance > 0:           # if trying to go north-east
            direction = "north_east"
            return self.rec_check_if_path_clear(old_row, old_column, distance, counter, direction,
                                                new_row, new_column)

        if vertical_distance < 0 and horizontal_distance < 0:           # if trying to go north-west
            direction = "north_west"
            return self.rec_check_if_path_clear(old_row, old_column, distance, counter, direction,
                                                new_row, new_column)

        if vertical_distance > 0 and horizontal_distance > 0:           # if trying to go south-east
            direction = "south_east"
            return self.rec_check_if_path_clear(old_row, old_column, distance, counter, direction,
                                                new_row, new_column)


        if vertical_distance > 0 and horizontal_distance < 0:           # if trying to go south-west
            direction = "south_west"
            return self.rec_check_if_path_clear(old_row, old_column, distance, counter, direction,
                                                new_row, new_column)




    def check_if_can_capture(self, old_row, old_column, new_row, new_column):
        '''
        This method takes the current position and the next position as parameters to determine the direction.
        We also need to know where the footprint is going because apparently the rules for capturing stones
        when moving diagonal and moving straight, are different.
        When moving straight (north, south, east, west), we can capture stones only by the front row of our 3x3.
        If our "middle layer" (the center and the two sides beside it, depending on the direction) overlaps on
        obstacle, then it will return False because it can't catch further.
        As for diagonal moves, we can capture stones as long as the center of the footprint doesn't overlap with
        an obstacle, so the "wings" and the "head" all can capture stones.
        Also, we make an exception when moving only one block because the way this method mainly works is that it
        tries to see the new location if it has any obstacles and see if the center can safely land there. In the
        case of moving one block, however, if there are any stone in the front row of our 3x3 footprint, then
        it sees that there's an "obstacle" although it's probably just looking at its own stone.
        So this returns False for any illegal overlaps.
        '''

        horizontal_distance = new_column - old_column
        vertical_distance = new_row - old_row


        if vertical_distance < 0 and horizontal_distance == 0:    # if trying to go north
            if self._board[new_row][new_column] == '-':           # if the next center has no obstacle, but
                if self._board[new_row][new_column-1] != '-' or self._board[new_row][new_column+1] != '-':
                    return False                                  # if there is an obstacle at the side wings
            if self._board[new_row][new_column] != '-':           # then cannot catch further.
                if vertical_distance == -1:                       # if only moving one step, because it's safe to catch
                    return True                                   # with just the "frontline"
                return False

        elif vertical_distance > 0 and horizontal_distance == 0:  # if trying to go south
            if self._board[new_row][new_column] == '-':           # if the next center has no obstacle, but
                if self._board[new_row][new_column-1] != '-' or self._board[new_row][new_column+1] != '-':
                    return False                                  # if there is an obstacle at the side wings
            if self._board[new_row][new_column] != '-':           # then cannot catch further.
                if vertical_distance == 1:                        # if only moving one step, because it's safe to catch
                    return True                                   # with just the "frontline"
                return False

        elif vertical_distance == 0 and horizontal_distance > 0:  # if trying to go east
            if self._board[new_row][new_column] == '-':           # if the next center has no obstacle, but
                if self._board[new_row-1][new_column] != '-' or self._board[new_row+1][new_column] != '-':
                    return False                                  # if there is an obstacle at the side wings
            if self._board[new_row][new_column] != '-':           # then cannot catch further.
                if horizontal_distance == 1:                      # if only moving one step, because it's safe to catch
                    return True                                   # with just the "frontline"
                return False

        elif vertical_distance == 0 and horizontal_distance < 0:  # if trying to go west
            if self._board[new_row][new_column] == '-':           # if the next center has no obstacle, but
                if self._board[new_row-1][new_column] != '-' or self._board[new_row+1][new_column] != '-':
                    return False                                  # if there is an obstacle at the side wings
            if self._board[new_row][new_column] != '-':           # then cannot catch further.
                if horizontal_distance == -1:                     # if only moving one step, because it's safe to catch
                    return True                                   # with just the "frontline"
                return False

        else:                                                               # if it's going diagonal. Where it can
            if self._board[new_row][new_column] != '-':                     # capture with the "wings" and the "head"

                if vertical_distance == -1 and horizontal_distance == 1:    # if only moving one step north-east
                    return True
                if vertical_distance == -1 and horizontal_distance == -1:   # if only moving one step north-west
                    return True
                if vertical_distance == 1 and horizontal_distance == 1:     # if only moving one step south-east
                    return True
                if vertical_distance == 1 and horizontal_distance == -1:    # if only moving one step south-west
                    return True
                return False



    def clear_current_piece(self, old_row, old_column):
        '''
        This is a method used while "moving" a piece. When moving a piece, it saves the original 3x3 footprint,
        clears its old position, then the saved footprint is then placed in the new location.
        So this method is used for clearing those old positions of the footprint .
        It's like when you lift your stones with your hands,
        then there's nothing at their respective positions on the board.
        '''

        self._board[old_row][old_column] = '-'                  # clears the center
        self._board[old_row - 1][old_column] = '-'              # clears the north side
        self._board[old_row + 1][old_column] = '-'              # clears the south side
        self._board[old_row][old_column + 1] = '-'              # clears the east side
        self._board[old_row][old_column - 1] = '-'              # clears the west side
        self._board[old_row - 1][old_column + 1] = '-'          # clears the north-east side
        self._board[old_row - 1][old_column - 1] = '-'          # clears the north-west side
        self._board[old_row + 1][old_column + 1] = '-'          # clears the south-east side
        self._board[old_row + 1][old_column - 1] = '-'          # clears the south-west side



    def clear_edges(self):
        '''
        This method clears the edges of the board. Even though the board has to be 20x20, as per rule of the game,
        only the middle 18x18 can be used. If part of a piece gets off of the 18x18 board, then that piece is gone.
        So the way this works is that by the end of each make_move turn, it always clear the edges of the board,
        just in case any parts of pieces were placed on the edges. Also, this is used for before a test of whether if
        the player is trying to move his or her last ring off the board or not.
        '''

        for i in range(0, 20):  # clears top row
            self._board[0][i] = '-'

        for i in range(0, 20):  # clears bottom row
            self._board[19][i] = '-'

        for i in range(0, 20):  # clears left column
            self._board[i][0] = '-'

        for i in range(0, 20):  # clears right column
            self._board[i][19] = '-'



    def move_footprint(self, old_row, old_column, new_row, new_column):
        '''
        This method is kind of like the extension of the function make_move.
        Here, first we help check for obstacles ahead by "lifting our stones" so that we can see clear and don't mistake
        our footprint stones around us as obstacles.
        Second, we check our rings.
        So after attempting to move a piece, if it was a ring being moved and if it was moved off bounds, then
        invalidate the move and put everything back to where it was.
        Then we also check whether we have broken a ring when we lift a piece. If we broke our last ring, put
        everything back to where it was and invalidate the move by returning False.
        After checking all the restrictions and if it passes all of that then it can move depending on the restrictions.
        When moving, it saves the original footprint into temp, clears the old footprints location, then places it into
        the new location. It then clears the edges of debris, checks if each player's rings are still intact, if not,
        then declare a winner, otherwise it increments the counter for player_turn to pass the turn to the next player.
        '''


        ### Saves the current footprint to temp. ###

        center = self._board[old_row][old_column]
        north = self._board[old_row - 1][old_column]
        south = self._board[old_row + 1][old_column]
        east = self._board[old_row][old_column + 1]
        west = self._board[old_row][old_column - 1]
        north_east = self._board[old_row - 1][old_column + 1]
        north_west = self._board[old_row - 1][old_column - 1]
        south_east = self._board[old_row + 1][old_column + 1]
        south_west = self._board[old_row + 1][old_column - 1]


        ### Saves the prospective footprint to another temp. ###

        new_center = self._board[new_row][new_column]
        new_north = self._board[new_row - 1][new_column]
        new_south = self._board[new_row + 1][new_column]
        new_east = self._board[new_row][new_column + 1]
        new_west = self._board[new_row][new_column - 1]
        new_north_east = self._board[new_row - 1][new_column + 1]
        new_north_west = self._board[new_row - 1][new_column - 1]
        new_south_east = self._board[new_row + 1][new_column + 1]
        new_south_west = self._board[new_row + 1][new_column - 1]


        self.clear_current_piece(old_row, old_column)                   # "lift the stones up" / clear their positions


        if self.check_if_path_clear(old_row, old_column, new_row, new_column) is False:

            self._board[old_row][old_column] = center                   # We use "lift the stones" first before checking
            self._board[old_row - 1][old_column] = north                # for obstacles ahead. If we didn't lift, we
            self._board[old_row + 1][old_column] = south                # might step on our own foot, or our own stones.
            self._board[old_row][old_column + 1] = east                 # But if there is still indeed an obstacle ahead
            self._board[old_row][old_column - 1] = west                 # then do not go ahead with the plan
            self._board[old_row - 1][old_column + 1] = north_east       # and put the stones back.
            self._board[old_row - 1][old_column - 1] = north_west
            self._board[old_row + 1][old_column + 1] = south_east
            self._board[old_row + 1][old_column - 1] = south_west

            print("Obstacle ahead, can't get through.")
            return False


        ### if it's the black player's turn. ###

        if self._player_turn % 2 == 0:
            if (
                    (center == '-') and                                 # if the piece being moved is a ring
                    (north == 'B') and
                    (south == 'B') and
                    (east == 'B') and
                    (west == 'B') and
                    (north_east == 'B') and
                    (north_west == 'B') and
                    (south_east == 'B') and
                    (south_west == 'B')
            ):

                self._board[new_row][new_column] = center               # Go ahead first and put it to the new position.
                self._board[new_row - 1][new_column] = north
                self._board[new_row + 1][new_column] = south
                self._board[new_row][new_column + 1] = east
                self._board[new_row][new_column - 1] = west
                self._board[new_row - 1][new_column + 1] = north_east
                self._board[new_row - 1][new_column - 1] = north_west
                self._board[new_row + 1][new_column + 1] = south_east
                self._board[new_row + 1][new_column - 1] = south_west

                self.clear_edges()                                      # But if after the edges have been cleared,
                                                                        # and we find that our ring is broken, then that
                if self.check_own_rings() == False:                     # must have meant that the player moved it off
                                                                        # the board.
                    self._board[old_row][old_column] = center           # If so, put back everything in its original
                    self._board[old_row - 1][old_column] = north        # position and return False.
                    self._board[old_row + 1][old_column] = south        # If it didn't go off the board, execute the
                    self._board[old_row][old_column + 1] = east         # move, update the game status, pass the turn
                    self._board[old_row][old_column - 1] = west         # to the next player, then return True.
                    self._board[old_row - 1][old_column + 1] = north_east
                    self._board[old_row - 1][old_column - 1] = north_west
                    self._board[old_row + 1][old_column + 1] = south_east
                    self._board[old_row + 1][old_column - 1] = south_west

                    self._board[new_row][new_column] = new_center
                    self._board[new_row - 1][new_column] = new_north
                    self._board[new_row + 1][new_column] = new_south
                    self._board[new_row][new_column + 1] = new_east
                    self._board[new_row][new_column - 1] = new_west
                    self._board[new_row - 1][new_column + 1] = new_north_east
                    self._board[new_row - 1][new_column - 1] = new_north_west
                    self._board[new_row + 1][new_column + 1] = new_south_east
                    self._board[new_row + 1][new_column - 1] = new_south_west

                    return False

                self.update_game_status()

                self._player_turn += 1

                for i in game._board:
                    print(i)

                return True


        ### if it's the white player's turn. ###

        if self._player_turn % 2 == 1:
            if (
                    (center == '-') and                                 # if the piece being moved is a ring
                    (north == 'W') and
                    (south == 'W') and
                    (east == 'W') and
                    (west == 'W') and
                    (north_east == 'W') and
                    (north_west == 'W') and
                    (south_east == 'W') and
                    (south_west == 'W')
            ):

                self._board[new_row][new_column] = center               # Go ahead first and put it to the new position
                self._board[new_row - 1][new_column] = north
                self._board[new_row + 1][new_column] = south
                self._board[new_row][new_column + 1] = east
                self._board[new_row][new_column - 1] = west
                self._board[new_row - 1][new_column + 1] = north_east
                self._board[new_row - 1][new_column - 1] = north_west
                self._board[new_row + 1][new_column + 1] = south_east
                self._board[new_row + 1][new_column - 1] = south_west

                self.clear_edges()                                      # But if after the edges have been cleared,
                                                                        # and we find that our ring is broken, then that
                if self.check_own_rings() == False:                     # must have meant that the player moved it off
                                                                        # the board.
                    self._board[old_row][old_column] = center           # If so, put back everything in its original
                    self._board[old_row - 1][old_column] = north        # position and return False.
                    self._board[old_row + 1][old_column] = south        # If it didn't go off the board, execute the
                    self._board[old_row][old_column + 1] = east         # move, update the game status, pass the turn
                    self._board[old_row][old_column - 1] = west         # to the next player, then return True.
                    self._board[old_row - 1][old_column + 1] = north_east
                    self._board[old_row - 1][old_column - 1] = north_west
                    self._board[old_row + 1][old_column + 1] = south_east
                    self._board[old_row + 1][old_column - 1] = south_west

                    self._board[new_row][new_column] = new_center
                    self._board[new_row - 1][new_column] = new_north
                    self._board[new_row + 1][new_column] = new_south
                    self._board[new_row][new_column + 1] = new_east
                    self._board[new_row][new_column - 1] = new_west
                    self._board[new_row - 1][new_column + 1] = new_north_east
                    self._board[new_row - 1][new_column - 1] = new_north_west
                    self._board[new_row + 1][new_column + 1] = new_south_east
                    self._board[new_row + 1][new_column - 1] = new_south_west

                    return False

                self.update_game_status()

                self._player_turn += 1

                for i in game._board:
                    print(i)

                return True


        if self._player_turn % 2 == 0:                                  # if it's black player's turn

            if self.check_own_rings() == False:                         # if after we lift our stones up and then we
                                                                        # we noticed that we broke our ring,
                self._board[old_row][old_column] = center               # then put the stones back and return False
                self._board[old_row - 1][old_column] = north
                self._board[old_row + 1][old_column] = south
                self._board[old_row][old_column + 1] = east
                self._board[old_row][old_column - 1] = west
                self._board[old_row - 1][old_column + 1] = north_east
                self._board[old_row - 1][old_column - 1] = north_west
                self._board[old_row + 1][old_column + 1] = south_east
                self._board[old_row + 1][old_column - 1] = south_west

                return False

        if self._player_turn % 2 == 1:                                  # if it's white player's turn

            if self.check_own_rings() == False:                         # if after we lift our stones up and then we
                                                                        # we noticed that we broke our ring,
                self._board[old_row][old_column] = center               # then put the stones back and return False
                self._board[old_row - 1][old_column] = north
                self._board[old_row + 1][old_column] = south
                self._board[old_row][old_column + 1] = east
                self._board[old_row][old_column - 1] = west
                self._board[old_row - 1][old_column + 1] = north_east
                self._board[old_row - 1][old_column - 1] = north_west
                self._board[old_row + 1][old_column + 1] = south_east
                self._board[old_row + 1][old_column - 1] = south_west

                return False

        self._board[new_row][new_column] = center                       # If everything else is good, then execute the
        self._board[new_row - 1][new_column] = north                    # move, update the game status, pass the turn
        self._board[new_row + 1][new_column] = south                    # to the next player, then return True.
        self._board[new_row][new_column + 1] = east
        self._board[new_row][new_column - 1] = west
        self._board[new_row - 1][new_column + 1] = north_east
        self._board[new_row - 1][new_column - 1] = north_west
        self._board[new_row + 1][new_column + 1] = south_east
        self._board[new_row + 1][new_column - 1] = south_west

        self.clear_edges()

        self.update_game_status()

        self._player_turn += 1

        for i in game._board:
            print(i)

        return True



    def make_move(self, old_position, new_position):
        '''
        This is pretty much the main method, which takes the current and the new location as paramaters.
        Then it converts those parameters into row and column coordinates for easier navigation throughout the board.
        So this method mainly just checks and gives restrictions before a move is executed. Upon making a move,
        this method calls other functions to:

        check if current center or next center is placed on the off-bound edges of the board,
        checks if it only contains the player's stones and not the opponent's,
        checks whether desired direction is valid,
        checks whether the capturing move is valid,
        checks whether the footprint has a center or not to determine the allowance of the distance it can cover,
        check the rings if they have been broke through move_footprint and check_own_rings,
        checks whether the game has been over and somebody has already one, etc.

        After checking all the restrictions and if it passes all of that then it can move depending on the restrictions.
        If the player successfully makes the move after passing all restrictions, returns True.
        If the move didn't pass, then it's an illegal move and returns False.
        More details about the mechanics of checking rings and checking obstacles ahead at the move_footprint function.
        '''

        old_row = self.get_row(old_position)          # converts the current coordinates into row and column coordinates
        old_column = self.get_column(old_position)

        new_row = self.get_row(new_position)          # converts the next coordinates into row and column coordinates
        new_column = self.get_column(new_position)


        horizontal_distance = new_column - old_column
        vertical_distance = new_row - old_row         # calculates distance for matching with the center's existence

        if self.get_game_state() != "UNFINISHED":     # check if game over
            print("Game was over")
            return False

        elif self.check_boundary(old_row, old_column, new_row, new_column) is False:
            print("Center can't be out of bounds. Try again!")
            return False                              # check if center is placed outside of 18x18 board

        elif self.check_stones(old_row, old_column) is False:
            print("Your 3x3 footprint contains an opponent's stone. Try again!")
            return False                              # check if the footprint only has one's stones

        elif self.check_directions(old_row, old_column, new_row, new_column) is False:
            print("Check your stones for directions and try again!")
            return False                              # check if the direction going to is valid

        elif self.check_if_can_capture(old_row, old_column, new_row, new_column) is False:
            print("Can't catch further.")             # check how far a footprint can capture stones
            return False

        elif self.check_empty_center(old_row, old_column) is True:
            if abs(vertical_distance) <= 3:           # If the piece doesn't have a center stone, it can only move up to
                if abs(horizontal_distance) <= 3:     # 3 blocks

                    if self.move_footprint(old_row, old_column, new_row, new_column) == False:
                        return False
                    else:                             # this is a move for piece without a center stone
                        return True                   # If one's rings are still intact and there are no obstacles ahead
                                                      # execute move and return True, otherwise False.
                else:
                    print("Out of range. Try again!")
                    return False                      # The purpose of the vertical and horizontal distance checking
            else:                                     # if they're equal is to check a strict diagonal move.
                print("Out of range. Try again!")
                return False
        else:                                         # this is a move for piece with a center stone
            if self.move_footprint(old_row, old_column, new_row, new_column) == False:
                return False
            else:
                return True                           # If one's rings are still intact and there are no obstacles ahead
                                                      # execute move and return True, otherwise False.




game = GessGame()
state = game.get_game_state()



# ####################################################################
# ####################################################################
#
#                         ##GAMEPLAY TEST###
#
#
#
# for i in game._board:               # prints initial board
#     print(i)
#
#
# print('\n')
# print(game._player_turn)
# print(game.make_move('j6', 'g9')) # black 0
# print(game.get_game_state())
# print(game._player_turn)
# print(game.make_move('i15', 'i13')) # white 1
# print(game.get_game_state())
#
#
#
#
# print('\n')
# print(game._player_turn)
# print(game.make_move('i3', 'i6')) # black 2
# print(game.get_game_state())
#
# print(game._player_turn)
# print(game.make_move('i18', 'i14')) # white 3
# print(game.get_game_state())
#
#
#
# print('\n')
# print(game._player_turn)
# print(game.make_move('r6', 'r9')) # black 4
# print(game.get_game_state())
#
# print(game._player_turn)
# print(game.make_move('f18', 'g17')) # white 5
# print(game.get_game_state())
#
#
#
# print('\n')
# print(game._player_turn)
# print(game.make_move('r3', 'r6')) # black 6
# print(game.get_game_state())
#
# print(game._player_turn)
# print(game.make_move('b15', 'c14')) # white 7
# print(game.get_game_state())
#
#
#
# print('\n')
# print(game._player_turn)
# print(game.make_move('r9', 'r10')) # black 8
# print(game.get_game_state())
#
# print(game._player_turn)
# print(game.make_move('p15', 'm12')) # white 9
# print(game.get_game_state())
#
#
#
# print('\n')
# print(game._player_turn)
# print(game.make_move('r10', 'r13')) # black 10
# print(game.get_game_state())
#
# print(game._player_turn)
# print(game.make_move('r18', 'r15')) # white 11
# print(game.get_game_state())
#
#
#
# print('\n')
# print(game._player_turn)
# print(game.make_move('r6', 'r13')) # black 12
# print(game.get_game_state())
#
# print(game._player_turn)
# print(game.make_move('l18', 'j18')) # white 13
# print(game.get_game_state())
#
#
#
# print('\n')
# print(game._player_turn)
# print(game.make_move('o6', 'o9')) # black 14
# print(game.get_game_state())
#
# print(game._player_turn)
# print(game.make_move('k11', 'n11')) # white 15
# print(game.get_game_state())
#
#
#
# print('\n')
# print(game._player_turn)
# print(game.make_move('r13', 'm13')) # black 16
# print(game.get_game_state())
#
# print(game._player_turn)
# print(game.make_move('i14', 'k14')) # white 17
# print(game.get_game_state())
#
#
#
# print('\n')
# print(game._player_turn)
# print(game.make_move('n13', 'm14')) # black 18
# print(game.get_game_state())
#
# print(game._player_turn)
# print(game.make_move('j14', 'k14')) # white 19
# print(game.get_game_state())
#
#
#
# print('\n')
# print(game._player_turn)
# print(game.make_move('i6', 'h6')) # black 20
# print(game.get_game_state())
#
# print(game._player_turn)
# print(game.make_move('k14', 'l14')) # white 21
# print(game.get_game_state())
#
#
#
#
#
# print('\n')
# print(game._player_turn)
# print(game.make_move('h6', 'j6')) # black 22
# print(game.get_game_state())
# print(game._player_turn)
# print(game.make_move('l14', 'l8')) # white 23
# print(game.get_game_state())
#
#
#
#
# print('\n')
# print(game._player_turn)
# print(game.make_move('j6', 'k6')) # black 24
# print(game.get_game_state())
#
# print(game._player_turn)
# print(game.make_move('o12', 'o9')) # white 25
# print(game.get_game_state())
#
#
#
# print('\n')
# print(game._player_turn)
# print(game.make_move('k6', 'l6')) # black 26
# print(game.get_game_state())
#
# print(game._player_turn)
# print(game.make_move('m9', 'l8')) # white 27
# print(game.get_game_state())
#
#
#
# print('\n')
# print(game._player_turn)
# print(game.make_move('o3', 'q5')) # black 28
# print(game.get_game_state())
#
# print(game._player_turn)
# print(game.make_move('l8', 'l7')) # white 29
# print(game.get_game_state())
#
#
#
# print('\n')
# print(game._player_turn)
# print(game.make_move('q5', 'o7')) # black 30
# print(game.get_game_state())
#
# print(game._player_turn)
# print(game.make_move('k7', 'k6')) # white 31
# print(game.get_game_state())
#
#
#
# print('\n')
# print(game._player_turn)
# print(game.make_move('l3', 'o3')) # black 32
# print(game.get_game_state())
#
# print(game._player_turn)
# print(game.make_move('k6', 'l5')) # white 33
# print(game.get_game_state())
#
#
#
# print('\n')
# print(game._player_turn)
# print(game.make_move('o3', 'r3')) # black 34
# print(game.get_game_state())
#
# print(game._player_turn)
# print(game.make_move('l5', 'n3')) # white 35
# print(game.get_game_state())
#
#
#
# print('\n')
# print(game._player_turn)
# print(game.make_move('o7', 'p6')) # black 36
# print(game.get_game_state())
#
# print(game._player_turn)
# print(game.make_move('n3', 'p3')) # white 37
# print(game.get_game_state())
#

#
# ####################################################################
# ####################################################################
#

