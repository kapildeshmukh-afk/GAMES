from turtle import Turtle
INITIAL_X_Y_COR = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snake = []
        self.createSnake()
        self.snakeHead=self.snake[0]
        self.snaketail=self.snake[-1]


    def createSnake(self):
        for position in INITIAL_X_Y_COR:
            self.addSnakeSegment(position)
    def addSnakeSegment(self,position):
            snakeSegment = Turtle(shape="square")
            snakeSegment.penup()
            snakeSegment.goto(position)
            snakeSegment.color("white")
            self.snake.append(snakeSegment)

    def extendSnake(self):
        self.addSnakeSegment(self.snake[-1].position())
 
    def move(self):
        for seg in range(len(self.snake) - 1, 0, -1):
            newXcor = self.snake[seg - 1].xcor()
            newYcor = self.snake[seg - 1].ycor()
            self.snake[seg].goto(newXcor, newYcor)
        self.snakeHead.forward(MOVE_DISTANCE)
    def reset(self):
        for snakeSeg in self.snake:
            snakeSeg.goto(1000,1000)
        self.snake.clear()
        self.createSnake()
        self.snakeHead=self.snake[0]

    def up(self):
        if self.snakeHead.heading() != DOWN:
            self.snakeHead.setheading(90)
    def down(self):
        if self.snakeHead.heading() != UP:
            self.snakeHead.setheading(270)
    def left(self):
        if self.snakeHead.heading() != RIGHT:
            self.snakeHead.setheading(180)
    def right(self):
        if self.snakeHead.heading() != LEFT:
            self.snakeHead.setheading(0)
