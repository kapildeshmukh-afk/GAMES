from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

#SCREEN PROPERTIES
scr= Screen()
scr.setup(width=700, height=700)
scr.title("Make @ Snake")
scr.tracer(0)
scr.bgcolor("black")

#CREATING all OBJECT
snakemodel = Snake()
foodmodel = Food()
scoremodel = ScoreBoard()


#for  adding keypress function to the CODE
scr.listen()
scr.onkey(snakemodel.up, "Up")
scr.onkey(snakemodel.down, "Down")
scr.onkey(snakemodel.left, "Left")
scr.onkey(snakemodel.right, "Right")
playing = True
while playing:
    scr.update()
    time.sleep(0.1)
    snakemodel.move()
    #DETECTING COLLISION WITH FOOD
    if snakemodel.snakeHead.distance(foodmodel)<15:
        foodmodel.refresh()
        scoremodel.increaseScore()
        snakemodel.extendSnake()
    #DETECTING COLLISION WITH WALL
    if snakemodel.snakeHead.xcor() > 335 or snakemodel.snakeHead.xcor() < -335 or snakemodel.snakeHead.ycor() > 335 or snakemodel.snakeHead.ycor() < -335:
        snakemodel.reset()
        scoremodel.reset()


    #DETECT COLLISION WITH TAIL
    for collisionPart in snakemodel.snake[1:]:
        if snakemodel.snakeHead.distance(collisionPart) < 10:
            snakemodel.reset()
            scoremodel.reset()

scr.exitonclick()