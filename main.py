from game import Game
from minion import Minion

def main():
    game = Game()
    for i in range(len(game.players)):
        name =  game.players[i-1]
        minion = Minion(name)
    if game.game_continue:
        game.draw()
        game.gather_players()
        for i in range(len(game.players)):
            job = game.pick_job()
            game.players[i].job = job

            #TODO make minions work and eat
            #TODO When does the game end
        for i in range(game.round):
            minion.work()
            minion.eating()
            
            game.round += 1

            if game.round == "10":
                print("game over")

if __name__ == "__main__":
    main()