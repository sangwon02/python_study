print("공이 튀긴횟수를 알려드립니다.")
h=int(input("높이를 입력하세요(m):"))
jump=0    #공이 튀긴횟수는 0부터
while True:
    jump=jump+1 #한번튀길때마다 jump에 1을 더해줌
    h = h*0.5 #높이가 반으로 줄음
    if h<0.00001:#일정값 이하가 되면 멈춤
        break
print("공이 튀긴 횟수는",jump,"입니다")
