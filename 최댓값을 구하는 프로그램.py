print("정수를 입력하시면 최댓값을 찾아드립니다.(5개의 숫자만 입력가능)")
a = int(input("정수를 입력하세요.:"))
b = int(input("정수를 입력하세요.:"))
c = int(input("정수를 입력하세요.:"))
d = int(input("정수를 입력하세요.:"))
e = int(input("정수를 입력하세요.:"))

math_score = [a, b, c, d, e]

maxlist = math_score[0]
for i in range(1, len(math_score)):
    if maxlist < math_score[i]:
        maxlist = math_score[i]
print("최댓값은",maxlist,"입니다.")
