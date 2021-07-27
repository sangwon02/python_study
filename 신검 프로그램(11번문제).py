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
