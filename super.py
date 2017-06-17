import random as r
class Fish:
    def __init__(self):
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)
    def move(self):
        self.x -=1
        print("我的位置:",self.x,self.y)
class GoldFish(Fish):
    pass
class Carp(Fish):
    pass
class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.hungry=True
    def eat(self):
        print("好吃")
