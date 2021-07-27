from turtle import*
from ballclass import Ball  #볼클래스를 불러온다.

redball = Ball("red", 1, 10, 10)#공에 대한 성분을 넣어준다.
blueball = Ball("blue", 2, 7, 7)

while True: #공이 무수히 움직이도록 무한 반복한다.
    redball.move()
    blueball.move()
