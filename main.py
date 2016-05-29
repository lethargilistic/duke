from duke import Game
from view import View
from interface import Controller

def main():
    m = Game()
    v = View(m)
    c = Controller(m, v)

    still_playing = True
    while(still_playing == True):
        still_playing = c.game_loop()
    #Game is over.

if __name__ == "__main__":
    main()
