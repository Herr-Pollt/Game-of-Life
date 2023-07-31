import random

class Minion():
    def __init__(self, name):
        self.name = name
        self.salary = 0
        self.balance = 0
        self.hunger = 10
    def work(self):
        self.balance += self.salary
        print(f"""You are working very hard and has gained {self.salary} 
              dollars.That would mean that you have {self.balance} dollars.""")
    def eating(self):
        work_efficiency = random.randint(1, 3)
        print(f"""You have been pretty lazy at work so your hunger got depleted by two""")