import random

class Minion():
    def __init__(self, name):
        self.name = name
        self.salary = 0
        self.balance = 0
        self.hunger = 10
        self.job = "thief"
        self.jobs = ["firefighter", "farmer", "professor", "gamer", "thief"]

    def work(self):
        boss_notice = random.randint(1, 3)
        self.balance += self.salary

        print(f"You are working very hard and have gained {self.salary} dollars."
              f"That would mean that you have {self.balance} dollars.")

        if boss_notice == 3:
            job_opportunity = input("Your boss notices that you have been working extra hard and you have done "
                                    "a great job. He offers you a promotion of 10k, but another company offers you "
                                    "a job opportunity. Do you take the job opportunity (y/n)?")

            if job_opportunity.lower() in ["y", "yes"]:
                self.job = random.choice(self.jobs)

            elif job_opportunity.lower() in ["n", "no"]:
                print("Your salary has been added by 10k!")
                self.salary += 10

            else:
                print("Sorry, but that is an invalid answer")

    def eating(self):
        work_efficiency = random.randint(1, 3)
        if work_efficiency == 1:
            print("You have been pretty lazy at work so your hunger got depleted by two")
            self.hunger -= 2

        elif work_efficiency == 2:
            print("The boss knows that you have done all your requirements "
                  "and have been working very hard, so your hunger got depleted by 4")
            self.hunger -= 4

        elif work_efficiency == 3:
            print("You have been an extremely good worker today and "
                  "you felt like your really have done a lot of things, "
                  "so your hunger gets depleted by 6")
            self.hunger -= 6

        hunger_check = input("Do you want to check your hunger? (y/n)")

        if hunger_check.lower() in ["y", "yes"]:
            print(f"Your hunger is {self.hunger}")

