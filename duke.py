from pieces import Duke, Footman

class Game():
    def __init__(self):
        self.board_size = 6
        self.board = [["  " for x in range(self.board_size)] for y in range(self.board_size)]
        self.active_player = 1
        
        self.players = [None, None, None] #No Player 0
        self.create_player(1)
        self.create_player(2)

    def create_player(self, player_number):
        right_or_left_for_duke = input("Place Duke on 1)Right or 2)Left?")
        if right_or_left_for_duke == "1":
            x = 2
        elif right_or_left_for_duke == "2":
            x = 3
        else:
            raise IndexError("Choose Right or left")
        if player_number == 1:
            y = 0
        elif player_number == 2:
            y = 5
        else:
            raise IndexError("Player should be 1 or 2")

        duke = Duke(x,y,player_number)
        footman1 = Footman(x+1,y,player_number)
        footman2 = Footman(x-1,y,player_number)
        self.board[duke.get_y()][duke.get_x()] = id(duke)
        self.board[footman1.get_y()][footman1.get_x()] = id(footman1)
        self.board[footman2.get_y()][footman2.get_x()] = id(footman2)
        self.players[player_number] = {id(duke):duke, id(footman1):footman1, id(footman2):footman2}

    def display_board(self):
        #TODO: Couple this loosely
        for piece in self.players[1]:
            x = self.players[1][piece].get_x()
            y = self.players[1][piece].get_y()
            self.board[y][x] = str(self.players[1][piece])
        for piece in self.players[2]:
            x = self.players[2][piece].get_x()
            y = self.players[2][piece].get_y()
            self.board[y][x] = str(self.players[2][piece])
        count = 0
        for row in self.board:
            print(str(count), end="")
            count+=1
            for slot in row:
                print(slot + "|", end="")
            print()

    def game_loop(self):
        #Each player has a list of pieces. If no Duke in their pieces, they lose
        still_playing = True
        #TODO: remove temporary import below
        import time
        while(still_playing):
            #Display Board
            self.display_board()
            #Choose piece to move
            #Highlight possible moves
            #Choose move
            print("CHOOSE MOVE")
            time.sleep(2)
            #Execute move
            #Is game over?
            #End of turn housekeeping
            #moved_piece.change_side()
            #self.active_player = self.active_player % 2 + 1
        #Game is over. Show results

g = Game()
g.game_loop()
