import random

tries = 0
guess = 0;
answer = random.randint(1, 100)

print("1부터 100 사이의 숫자를 맞추시오.(가회는 7번)")

while tries < 7:
    guess = int(input("숫자를 입력하시오: "))
    tries = tries + 1
    if guess < answer:
        print("더 높은 숫자를 입력하세요!")
    elif guess > answer:
        print("더 낮은 숫자를 입력하세요!")
    if guess == answer:
        print("축하합니다. 시도횟수=", tries)
        
else:
    print("주어진 기회를 다 사용하였습니다. 정답은 ", answer)
