from turtle import*

class Ball:  #볼에 대한 기본 성분에 대한 바탕
    def __init__(self, color, size, xspeed, yspeed):
        self.x = 0
        self.y = 0
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.size = size
        self.color = color
        self.turtle = Turtle()
        self.turtle.shape("circle")
        self.turtle.color(color, color)
        self.turtle.resizemode("user")
        self.turtle.shapesize(size, size, 10)
        self.turtle.penup()

    def move (self): #움직였을 때 어떻게 움직일 것인지설정
        self.x += self.xspeed
        self.y += self.yspeed
        self.turtle.goto(self.x, self.y)
        if self.x > 500 or self.x < -500:
            self.xspeed = -self.xspeed
        if self.y > 400 or self.y < -400:
            self.yspeed = -self.yspeed
