import random

quotes = []

quotes.append("가는 말이 고와야 오는 말이 곱다.")
quotes.append("시작이 반이다.")
quotes.append("피할 수 없다면 즐겨라.")
quotes.append("인내는 쓰고 열매는 달다.")
quotes.append("말 안 하면 귀신도 모른다.")
quotes.append("굼벵이도 구르는 재주가 있다.")
quotes.append("남의 떡이 커보인다.")
quotes.append("계란으로 바위치기")

dailyQuate = random.choice(quotes)
print("#############################")
print("#오늘의 속담#")
print("#############################")
print("")
print(dailyQuate)
