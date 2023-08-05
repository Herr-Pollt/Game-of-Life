import art
from minion import Minion
import random

class Game():
    
    def __init__(self) -> None:
        self.round = 0
        self.players = []
        self.jobs = ["firefighter", "farmer", "professor", "gamer", "thief"]

    def pick_job(self, minion):
        chosen_jobs = random.sample(self.jobs, 2)
        job = input(f"""Your two choices of jobs are {chosen_jobs[0]} and {chosen_jobs[1]},
                     Press 1 for the first job, press 2 for the second job""")
        job = chosen_jobs[job - 1]

    def gather_players(self):
        player_amount= int(input("How many players would like to play?"))
        if player_amount <= 1:
            print("Invalid! That is too less")
        if player_amount >= 5:
            print("Invalid! That is too many players")
        for i in range(player_amount):
            self.players.append(f"player{i+1}")
    
    def draw(self):
        art.tprint("Welcome to Minions'Life", "doom",True,  "chess1")