from minion import Minion
from game import Game

def main():
    game = Game()
    game.gather_players()
    game.draw()
    game.pick_job("Bob")

if __name__ == "__main__":
    main()