class Game():
    def __init__(self) -> None:
        self.round = 0
        self.players = []
    def gather_players(self):
        player_amount= input("How many players would like to play?")
        if player_amount <= 1:
            print("Invalid! That is too less")
        if player_amount >= 5:
            print("Invalid! That is too many players")
        for i in range(player_amount):
            self.players.append(f"player{i+1}")