import turtle
t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("", "도형을 입력하시오: ")
if s == "사각형" :
    s = turtle.textinput("", "가로: ")
    w=int(s)
    s = turtle.textinput("", "세로: ")
    h=int(s)
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)
    
if s == "삼각형" :
    s = turtle.textinput("", "변의 길이")
    w=int(s)
    t.forward(w)
    t.left(120)
    t.forward(w)
    t.left(120)
    t.forward(w)

if s == "원" :
    s = turtle.textinput("", "원의 크기")
    w=int(s)
    t.circle(w)
