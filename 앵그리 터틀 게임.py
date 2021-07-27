import turtle
import random
import math

player = turtle.Turtle()
player.shape("turtle")
screen = player.getscreen()

target = turtle.Turtle()
target.color("red")
target.shape("circle")
target.penup()
target.speed(0)
target.goto(random.randint(-100,100), random.randint(0,100))
speed = int(turtle.textinput("title","거북이 초기속도"))

def turnleft():
    player.left(5)

def turnright():
    player.right(5)

def play():
    player.forward(2)
    target.forward(2)
    screen.ontimer(play, 10)
    
screen.ontimer(play,10)
screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.listen()

def fire():
    x = 0
    y = 0
    velocity = speed
    angle = player.heading()
    vx = velocity * math.cos(angle * 3.14 / 180.0)
    vy = velocity * math.sin(angle * 3.14 / 180.0)
    while player.ycor() >= 0 :
        vx = vx
        vy = vy - 10
        x = x + vx
        y = y + vy
        player.goto(x, y)

screen.onkeypress(fire, "space")

