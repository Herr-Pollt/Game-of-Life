from game import Game
from minion import Minion

def main():
    game = Game()
    for i in range(len(game.players)):
        name = game.players[i].name
        minion = Minion(name)
        game.players[i] = minion

    if game.game_continue:
        game.draw()
        game.gather_players()
        for player in game.players:
            job = game.pick_job()
            player.job = job
        while game.round < 10:
            for player in game.players:
                choice = player.choice()
                if choice == "Rest":
                    pass
                elif choice == "Eat":
                    player.eat()
                elif choice == "Work":
                    player.job_check()
                    player.work()
                    player.hungry()
                print("---------------------------------------------")
            game.round += 1

        print("Game over")

if __name__ == "__main__":
    main()