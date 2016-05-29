from duke import Game
from view import View
from interface import Controller

#TODO: remove temporary import below
import time

def game_loop(view, controller):
    #Each player has a list of pieces. If no Duke in their pieces, they lose
    view.show_board()
    winner = 0
    while(winner == 0):
        winner = controller.take_turn()

        #Display Board
        view.show_board()
    #Game is over. Show results
    print("Player", winner, "wins!")

if __name__ == "__main__":
    m = Game()
    v = View(m)
    c = Controller(m)
    game_loop(v, c)
