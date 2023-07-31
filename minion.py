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
        if work_efficiency == 1:
            print(f"""You have been pretty lazy at work so your hunger got depleted by two""")
            self.hunger -= 2
        elif work_efficiency == 2:
            print(f"""The boss knows that you have done all your requirements and have been working very hard, so your hunger got depleted by 4""")
            self.hunger -= 2
        elif work_efficiency == 3:
            print(f"""You have been an extremely good worker today and you felt like your really have done a lot of things, so your hunger gets depleted by 6""")
            self.hunger -= 2