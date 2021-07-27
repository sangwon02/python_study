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
    

