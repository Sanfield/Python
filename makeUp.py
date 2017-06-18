class Turtle:
    def __init__(self,x):
        self.num=x
class Fish:
    def __init__(self,y):
        self.num=y

class Poll:
    def __init__(self,x,y):
        self.turtle=Turtle(x)
        self.fish=Fish(y)
    def print(self):
        print("水池里一共有 %d 只乌龟，%d 只小鱼" %(self.turtle.num,self.fish.num))
