from abc import ABC

class Job(ABC):
    def __init__(self, salary, name):
        super().__init__()
        self.salary = salary
        self.name = name

class Firefighter(Job):
    def __init__(self):
        super().__init__(20, "firefighter")


class Farmer(Job):
    def __init__(self):
        super().__init__(50, "farmer")

class Professor(Job):
    def __init__(self):
        super().__init__(40, "professor")

class Gamer(Job):
    def __init__(self):
        super().__init__(30, "gamer")

class Thief(Job):
    def __init__(self):
        super().__init__(5, "thief")