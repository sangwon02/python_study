print("두점 좌표의 거리를 알려드립니다. (x1, y1),(x2, y2)")
x1=int(input("x1:"))#일단 좌표를 받은뒤
y1=int(input("y1:"))
x2=int(input("x2:"))
y2=int(input("y2:"))

x3 = (x1-x2)**2#두점사이의 거리 구하는 공식을 통해 구한뒤 프린트한다.
y3 = (y1-y2)**2
print("두점 사이의 거리 : ", (x3+y3)**(1/2))
