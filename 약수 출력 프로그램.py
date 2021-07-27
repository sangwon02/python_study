x = int(input("정수를 입력하세요. 약수를 알려드립니다."))
for a in range(1, x+1 ):
    if x % a == 0:
        print(a,"(은)는 약수")

