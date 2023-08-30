import art
import random
from minion import Minion
class Game():
    
    def __init__(self) -> None:
        self.game_continue = True
        self.round = 0
        self.players = []
        self.jobs = ["firefighter", "farmer", "professor", "gamer", "thief"]


    def pick_job(self):
        chosen_jobs = random.sample(self.jobs, 2)
        job = int(input(f"""Your two choices of jobs are {chosen_jobs[0]} and {chosen_jobs[1]},
        Press 1 for the first job, press 2 for the second job"""))
        job = chosen_jobs[job - 1]
        
        return job

    def gather_players(self):
        player_amount= int(input("How many players would like to play?"))
        if player_amount <= 1:
            print("Invalid! That is too less")
        if player_amount >= 5:
            print("Invalid! That is too many players")
        for i in range(player_amount):
            name = input("Please enter a name for the charecter")
            minion = Minion(name)
            self.players.append(minion)
            
    
    def draw(self):
        art.tprint("Welcome to Minions'Life", "doom",True,  "chess1")