for i in range(1,int(input("2부터 원하시는 숫자 사이의 소수를 구해드립니다."))):
    for j in range(2, i+1):#2에서부터 계속 소수를 구하고 만약 i와j가 같아진다면 멈춘다.
        if (j == i):
            print(i)
        elif (i % j == 0):
            break
