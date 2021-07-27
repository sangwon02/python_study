import random

### 9번 문제
class Calculator:           # 9번 문제 클래스 
    ##### 여기에 코드를 작성하세요 #####
	def add(self, number1, number2): #더하기
		return number1 + number2

	def subtract(self, number1, number2): #차 구하기
		return number1 - number2

	def multipleple(self, number1, number2): #곱하기
		return number1 * number2

	def divide(self, number1, number2):#나누기
		return number1 / number2

    def mean(self, number1, number2):#평균 구하기
        return (number1 + number2)/2
    ##### 여기에 코드를 작성하세요 #####

print('여기서부터는 9번문제의 실행부분 입니다.') 
calc = Calculator(30,20)
print('두 수의 합은', calc.add())
print('두 수의 차는', calc.subtract())
print('두 수의 곱은', calc.multipleple())
print('두 수의 나눗셈은', calc.divide())
print('두 수의 평균은', calc.mean())


### 10번 문제
class Dice:                 # 10번 문제 클래스 
    def __init__(self):     # numberbers라는 빈 리스트 생성 
        self.numberbers = []   

    def playDice(self):     # 주사위 던지는 행위 (1에서 6사이의 랜덤값을 생성하여 numberbers 리스트에 append) 
        self.numberbers.append(random.randint(1,6))

    def getnumberbers(self):   # numberbers 리스트에 있는 내용 반환 
        return self.numberbers

    def getSum(self):       # numberbers 리스트에 있는 값들의 합을 반환
        return sum(self.numberbers)

def findSortedIndex(A):     # A리스트를 오름차순 정렬했을때 인덱스 ex) A=[5,9,6]이라면 이 함수의 반환값은 [0 2 1]
    return [i for (v, i) in sorted((v, i) for (i, v) in enumerate(A))]


print('\n여기서부터는 10번문제의 실행부분 입니다.')

gamer1Dice = Dice()     # 주사위 클래스를 이용하여 Gamer 1의 객체 생성 
gamer2Dice = Dice()     # 주사위 클래스를 이용하여 Gamer 2의 객체 생성
gamer3Dice = Dice()     # 주사위 클래스를 이용하여 Gamer 3의 객체 생성

for i in range(5):          # For 문을 도는 동안 각 Gamer가 주사위를 5번 던짐 
    gamer1Dice.playDice()   # Gamer 1가 주사위를 던짐
    gamer2Dice.playDice()   # Gamer 2가 주사위를 던짐
    gamer3Dice.playDice()   # Gamer 3가 주사위를 던짐

##### 여기에 코드를 작성하세요 #####
print("게이머1:", gamer1Dice.playDice)
print("게이머1의 합:", gamer1Dice.getSum)
print("게이머2:", gamer2Dice.playDice)
print("게이머2의 합:", gamer2Dice.getSum)
print("게이머3:", gamer3Dice.playDice)
print("게이머3의 합:", gamer3Dice.getSum)
sum1 = {"게이머1": gamer1Dice.getSum, "게이머2":gamer2Dice.getSum, "게이머3":gamer3Dice.getSum}
sum2 = sorted(sum.keys())
print = ("순위 순서대로", sum2)
##### 여기에 코드를 작성하세요 #####



### 11번문제
def unit_fraction(frac):    # 11번 문제 함수
    ##### 여기에 코드를 작성하세요 #####
    

    ##### 여기에 코드를 작성하세요 #####
    
print('\n여기서부터는 11번문제의 실행부분 입니다.') 
f_val = float(input("1보다 작고 0보다 큰 소수를 입력하세요: ")) # 입력 값 받기

if f_val <= 0.0 or f_val > 1.0 :
    print('입력 오류입니다.')
else :
    nf = unit_fraction(f_val)
    print('가장 가까운 단위분수는 1/{0}이며, 이 값은 {1:.5f}입니다.'.format(nf, 1/nf))

     
