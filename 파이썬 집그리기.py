Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t=turtle.Turtle()
>>> size=int(input("집의 크기는 얼마 할까요?"))
집의 크기는 얼마 할까요?100
>>> t.forward(size)
>>> t.right(90)
>>> t.forward(size)
>>> t.right(90)
>>> t.forward(size)
>>> t.right(90)
>>> t.forward(size)
>>> t.right(30)
>>> t.forward(size)
>>> t.right(30)
>>> t.right(30)
>>> t.right(30)
>>> t.forward(size)
>>> undo()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    undo()
NameError: name 'undo' is not defined
>>> t.undo()
>>> t.right(30)
>>> t.forward(size)
>>> 