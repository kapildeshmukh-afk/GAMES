from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("data.txt") as data:
            self.highScore = int( data.read())
        self.penup()
        self.color("white")
        self.goto(0, 310)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score : {self.highScore} ", align = ALIGNMENT , font = FONT)
    def increaseScore(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.highScore}")
        self.score = 0
        self.update_scoreboard()


