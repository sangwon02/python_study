#midterm_(2021124126)_(이상원)

#함수정의 부분

#4번문제
a = int(input("첫번째 수를 입력하세요: "))
b = int(input("두번째 수를 입력하세요: "))

a, b = b,a #두수를 교환
print(a, b)

#5번문제

radius = float(input("반지름을 입력하세요:"))
PI=3.14
l=2*PI*radius

print("원의 둘레=",l)

radius = float(input("반지름을 입력하세요:"))
PI=3.14
area=PI*radius**2

print("원의 넓이=",area)


#6번문제

print("두수를 입력하시면 덧셈, 뺼셈, 곱셈, 나눗셈, 평균을 구해드립니다.")
a = int(input("첫번째 숫자를 입력하시오:  "))
b = int(input("두번째 숫자를 입력하시오:  "))
#a와b에 대해서 정보를 받은뒤 원하는 값을 프린트한다. 
print("덧셈", a+b)
print("뺼셈", a-b)
print("곱셈", a*b)
print("나눗셈", a/b)
print("평균", (a+b)/2)

#7번문제
print("2차방정식은 ax^2+bx+c의 해를 구해드립니다.")
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

D = (b**2) - (4*a*c)
    
if D>0:  #D>0 일때 해는 2개 임으로 2개를 구한다.
        x1 = (-b + D**(1/2)) / (2*a)
        x2 = (-b - D**(1/2)) / (2*a)
        print("해의 갯수는  2개입니다, {} 또는 {} 입니다.".format(x1,x2))
elif D==0:   #D==0 일때 해는 1개 임으로 1개를 구한다.
        x = -b / 2*a
        print("해의 갯수는 1개 입니다. 해는 {}입니다.". format(x))
else:     #D<0 일때 해는 허근이다.
        print("해의 갯수는 0개 입니다.(허근)")

#8번문제
        
print("두점 좌표의 거리를 알려드립니다. (x1, y1),(x2, y2)")
x1=int(input("x1:"))#일단 좌표를 받은뒤
y1=int(input("y1:"))
x2=int(input("x2:"))
y2=int(input("y2:"))

x3 = (x1-x2)**2#두점사이의 거리 구하는 공식을 통해 구한뒤 프린트한다.
y3 = (y1-y2)**2
print("두점 사이의 거리 : ", (x3+y3)**(1/2))

#10번번문제
print("공이 튀긴횟수를 알려드립니다.")
h=int(input("높이를 입력하세요(m):"))
jump=0    #공이 튀긴횟수는 0부터
while True:
    jump=jump+1 #한번튀길때마다 jump에 1을 더해줌
    h = h*0.5 #높이가 반으로 줄음
    if h<0.00001:#일정값 이하가 되면 멈춤
        break
print("공이 튀긴 횟수는",jump,"입니다")

#11번문제
w = int(input("몸무게를 입력하시오.(단위:kg):"))
m = float(input("키를 입력하시오.(단위m):"))
bmi = w/(m**2)

if m <= 1.40: #키로 먼저 분리해 if-else문을 쓴다.
    print("6급입니다.")
    
elif 1.40 < m <1.46:
    print("5급입니다.")
    
elif 1.46 <= m <1.59:
    if 14 < bmi <49.9:#if-else구문에 다시 bmi로 if-else구문으로 나눈다,
        print("4급입니다.")
    else:
        print("5급입니다.")

elif 1.59 <= m < 1.61:
    if 17 < bmi <32.9:
        print("3급입니다.")
    elif 14 < bmi < 16.9 or 33 < bmi < 49.9:
        print("4급입니다.")
    else:
        print("5급입니다.")

elif 1.61 <= m <2.04:
    if 20 < bmi <24.9:
        print("1급입니다.")
    elif 18.5 < bmi < 19.9 or 25 < bmi < 29.9:
        print("2급입니다.")
    elif 17 < bmi < 18.4 or 30 < bmi < 32.9:
        print("3급입니다.")
    elif 14 < bmi < 16.9 or 33 < bmi < 49.9:
        print("4급입니다.")
    else:
        print("5급입니다.")
        
else:
    if 14 < bmi < 49.9:
        print("4급입니다.")
    else:
        print("5급입니다.")
#12번문제

for i in range(1,int(input("2부터 원하시는 숫자 사이의 소수를 구해드립니다."))):
    for j in range(2, i+1):#2에서부터 계속 소수를 구하고 만약 i와j가 같아진다면 멈춘다.
        if (j == i):
            print(i)
        elif (i % j == 0):
            break
#14번문제
        
print("*")
print("**")
print("***")
print("****")
print("*****")

#15번문제

sum1=0
sum2=0
for i in range(1, int(input("정수를 입력하시오.:"))):
    if i % 2 == 1:
        sum1+=i#홀수합을 구하는 식이다.
                            
    elif i % 2 == 0 :
        sum2+=i
        
    else: #정수를 안넣었을때에 이 구문이 나와야하는데 안나온다.......
        print("죄송합니다. 다시입력해주세요.")
        
m = input("어느합 알고 싶나요?(홀,짝이 아닌 입력값은 모든합): ")

if m == '홀':
    print("홀수합 :", sum1)
    
elif m == '짝':
    print("짝수합 :", sum2)
else: #홀,짝이 아닌 모든 경우는 모든합으로 대체한다.
    print("모든합:", sum1 + sum2)
    

