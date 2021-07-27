import datetime
#import numpy as np

# 3번 문제 함수 정의
def computeChange(inputMoney, totalPrice):  # 함수: 각 화페 단위의 거스름돈 계산 
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]    # 화페의 단위
    num = [0, 0, 0, 0, 0, 0, 0, 0]              # 각 화페의 거스름돈의 갯수
    inputMoney = int(input('받은 돈은? (10원을 최소단위로): '))
    totalPrice = int(input('물건값은? (10원을 최소단위로): '))
    change = inputMoney - totalPrice

    fifty_thousand = change//50000
    ten_thousand = (change % 50000) // 10000
    five_thousand = (change % 10000) // 5000
    thousand = (change % 5000) // 1000
    five_hundred = (change % 1000) // 500
    hundred = (change % 500) // 100
    fifty = (change % 100) // 50
    ten = (change % 50) // 10

    num[0]=fifty_thousand
    num[1]=ten_thousand
    num[2]=five_thousand
    num[3]=thousand
    num[4]=five_hundred
    num[5]=hundred
    num[6]=fifty
    num[7]=ten

    print("거스름돈은 ", change," 입니다.")
    print('필요한 각 화페 거스름돈의 갯수는 ...')
    for i in range(0,len(money)):               # 결과 출력
        print(money[i],' 원짜리 ', num[i], '개')

# 4번 문제 함수 정의
def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a

# 5번 문제 함수 정의
def sum_range(start, end, step):
    sum = start #각각 변수에 수를 알맞게 넣어줌
    sum_1 = start

    for i in range(1, (end-start)//step+1):#간격에 있는 횟수만큼 반복
        sum += step
        sum_1 += sum
    return sum_1

# 6번 문제 함수 정의
def find_max(lst):
    n = len(lst) #리스트 안에 있는 값 만큼 숫자를 줌
    max = lst[0]
    for i in range(1, n):#리스트의 안에 있는 값만큼 반복
        if lst[i] > max:#반복하면서 지금의 값보다 클경우 바꿔준다.
            max = lst[i]
    return max

def find_min(lst):
    n = len(lst)
    min = lst[0]
    for i in range(1, n):
        if lst[i] < min:
            min = lst[i]
    return min

# 7번 문제 함수 정의
def factorial(n):
    if n == 1:      # n이 1면
        return 1    # 1을 리턴하고 재귀호출을 끝낸다.
    return n * factorial(n - 1) # n과 함수에 n - 1을 넣어서 반환된 값을 곱한다.


# 3번 문제
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]    # 화페의 단위
num = [0, 0, 0, 0, 0, 0, 0, 0]              # 각 화페의 거스름돈의 갯수
inputMoney = int(input('받은 돈은? (10원을 최소단위로): '))
totalPrice = int(input('물건값은? (10원을 최소단위로): '))
computeChange(inputMoney, totalPrice)       # 함수 호출
print('필요한 각 화페 거스름돈의 갯수는 ...')
for i in range(0,len(money)):               # 결과 출력
    print(money[i],' 원짜리 ', num[i], '개')

# 4번 문제
print('필요한 상자의 갯수는 ', gcd(48,60), '개 입니다')

# 5번 문제
start = int(input('시작 정수 값은?'))
end = int(input('끝 정수 값은?'))
step = int(input('간격 정수 값은?'))
print(start, '에서 ', step, '간격으로 ', end,'까지 정수를 모두 더한 값은 ',sum_range(start, end, step), ' 입니다.')

# 6번 문제
A = [1, 9, 7, 6, 23, 45, 12, 5, 8, 28, 87, 67, 37, 4]
print('A 리스트에서 최대값은 ', find_max(A), '입니다')
print('A 리스트에서 최소값은 ', find_min(A), '입니다')

# 7번 문제
print("5! = ", factorial(5))
