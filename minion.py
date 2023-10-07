import random
import cutie
import jobs

class Minion():
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.hunger = 10
        self.job = ""
        self.salary = 0
    
    def job_check(self):
        if isinstance(self.job, jobs.Firefighter):
            self.salary = jobs.Firefighter().salary

        if jobs.Farmer().name == self.job:
            self.salary = jobs.Farmer().salary

        if jobs.Gamer().name == self.job:
            self.salary = jobs.Gamer().salary

        if jobs.Professor().name == self.job:
            self.salary = jobs.Professor().salary

        else:
            self.salary = jobs.Thief().salary

    def work(self):
        boss_notice = random.randint(1, 3)
        self.balance += self.salary

        print(f"{self.name}, you are working very hard and have gained {self.salary} dollars."
              f"That would mean that you have {self.balance} dollars.")
        print("""
--------------------------------------------------------------------------------------      
        """)
        if boss_notice == 3:
            job_opportunity = input(f"""{self.name}, your boss notices that you have been working extra hard and you have done 
            a great job. He offers you a promotion of $5, but another company offers you 
            a job opportunity. Do you take the job opportunity (y/n)?""")

            if job_opportunity.lower() in ["y", "yes"]:
                self.job = random.choice(self.jobs)

            elif job_opportunity.lower() in ["n", "no"]:
                print(f"{self.name}, your salary has been added by 5!")
                self.salary += 5

            else:
                print("Sorry, but that is an invalid answer")
            print("""
--------------------------------------------------------------------------------------      
            """)

    def hungry(self):
        work_efficiency = random.randint(1, 3)
        if work_efficiency == 1:
            print(f"{self.name}, you have been pretty lazy at work so your hunger got depleted by 1")
            self.hunger -= 1

        elif work_efficiency == 2:
            print(f"""{self.name} your boss knows that you have done all your requirements 
            and have been working very hard, so your hunger got depleted by 2""")
            self.hunger -= 2

        elif work_efficiency == 3:
            print(f"""{self.name}, you have been an extremely good worker today and
            you felt like your really have done a lot of things,
            so your hunger gets depleted by 3""")
            self.hunger -= 3
        print("""
--------------------------------------------------------------------------------------      
        """)

        hunger_check = input("Do you want to check your hunger? (y/n)")
        print("""
--------------------------------------------------------------------------------------      
        """)
        if hunger_check == "y" or "yes":
            print(f"Your hunger is {self.hunger}")

    def choice(self):
        if cutie.prompt_yes_or_no(f"Do you want to do things today, {self.name}?"):
            # List of names to select from, including some captions
            choices = [
                "Work",
                "Eat",
            ]
            # Get the choice
            choice = choices[cutie.select(choices)]
        else:
            choice = "rest"
        print(f"{self.name}, you chose {choice}")
        return choice
    
    def eat(self):
        food = []
        price = 0
        print("""Here is the menu
----------------------------------------------------------------------------""")
        if cutie.prompt_yes_or_no(f"Do you want an appetizer today, {self.name}?"):
            # List of names to select from, including some captions
            appetizer = [
                "Caesar Salad $3",
                "Fruit Salad $4",
                "Chedder Soup $3",
                "Seafood Soup $5",
            ]

            appetizer_choice = appetizer[cutie.select(appetizer)]

            if appetizer_choice == "Caesar Salad $3":
                price += 3
            elif appetizer_choice == "Fruit Salad $4":
                price += 4
            elif appetizer_choice == "Chedder Salad $3":
                price += 3
            elif appetizer_choice == "Seafood Salad $5":
                price += 5
            

            if self.balance < price:
                print("You have been denied for being too poor")
            else:
                food += appetizer_choice
                print(f"{self.name}, you chose {appetizer}")
        else:
            appetizer = "nothing"
        

        if cutie.prompt_yes_or_no(f"Do you want a main course today, {self.name}?"):
            main_course = [
                "Bob $1",
                "Buffalo Wings $3",
                "Spaghetti $5",
                "Steak $10",
                "Banana $10000",
            ]

            main_course_choice = main_course[cutie.select(main_course)]

            if main_course_choice == "Bob $1":
                price += 1
            elif main_course_choice == "Buffalo Wings $3":
                price += 3
            elif main_course_choice == "Spaghetti $5":
                price += 5
            elif main_course_choice == "Steak $10":
                price += 10
            elif main_course_choice == "Banana $10000":
                price += 10000
            
            food += main_course_choice

            if self.balance < price:
                    print("You have been denied for being too poor")
            else:
                food += main_course_choice
                print(f"{self.name}, you chose {main_course}")
        else:
            main_course = "nothing"

        if cutie.prompt_yes_or_no(f"Do you want dessert today, {self.name}?"):
            # List of names to select from, including some captions
            dessert = [
                "Ice Cream $2",
                "Creme Brulee $4",
                "Choclate Cake $4",
                "Sticky Toffee Pudding $6",
            ]
            
            dessert_choice = dessert

            if dessert_choice == "Ice Cream $2":
                price += 2
            elif dessert_choice == "Creme Brulee $4":
                price += 4
            elif dessert_choice == "Choclate Cake $4":
                price += 4
            elif dessert_choice == "Sticky Toffee Pudding $6":
                price += 6

            if self.balance < price:
                print("You have been denied for being too poor")
            else:
                food += dessert_choice
                print(f"{self.name}, you chose {dessert}")
        else:
            dessert = "nothing"
        self.balance -= price