from duke import Game
from view import View
from interface import Controller

#TODO: remove temporary import below
import time

def game_loop(view, controller):
    #Each player has a list of pieces. If no Duke in their pieces, they lose
    view.update()
    view.show_board()
    still_playing = True
    while(still_playing):
        still_playing = controller.make_move()

        #TODO: Remove temporary time advance
        time.sleep(2)

        #Display Board
        view.update()
        view.show_board()
    #Game is over. Show results

if __name__ == "__main__":
    m = Game()
    v = View(m)
    c = Controller(m)
    game_loop(v, c)