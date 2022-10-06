import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.75,stretch_wid=0.75)
        self.speed(0) #FASTEST
        self.refresh()
    def refresh(self):
        randomX = random.randint(-330, 330)
        randomY = random.randint(-330, 330)
        self.goto(randomX, randomY)