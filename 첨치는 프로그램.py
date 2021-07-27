import sys
import random

while True:
    name =input("이름: (종료하려면 엔터)")
    if name == "":
        sys.exit()

    question = input("무엇에 대해 알고 싶은가요? ")
    print(name+ "님" , question, "에 대하여 질문 주셨군요.")
    print("운명의 주사위를 굴려볼게요...")

    answers = random.randint(1, 8)

    if answers ==1:
        print ("네, 잘될것 입니다.")

    elif answers == 2:
        print ("가능성이 높아보입니다.")

    elif answers == 3:
        print ("좋아보입니다.")

    elif answers == 4:
        print ("글쎄요 잘모르겠네요.")

    elif answers == 5:
        print ("무조건 좋습니다.")

    elif answers == 6:
        print ("주사위가 NO입니다.")

    elif answers == 7:
        print ("너무 어려운 문제이네요.잫모르겠습니다.")

    else :
        print ("힘들어 보입니다.")

