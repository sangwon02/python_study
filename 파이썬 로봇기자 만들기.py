Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> stadium=input("경기장은 어디입니까?")
경기장은 어디입니까?서울
>>> winner=input("이긴팀은 어디입니까?")
이긴팀은 어디입니까?삼성
>>> loser=input("진팀은 어디입니까?")
진팀은 어디입니까?LG
>>> vip=input("우수선수는 누구입니까?")
우수선수는 누구입니까?홍길동
>>> score=input("스코어는 몇대몇입니까?")
스코어는 몇대몇입니까?8:7
>>> print("")

>>> print("=================")
=================
>>> print("오늘", stadium,"에서 야구 경기가 열렸습니다.")
오늘 서울 에서 야구 경기가 열렸습니다.
>>> print(winner, "과", loser, "은 치열한 공방전을 펼쳤습니다.")
삼성 과 LG 은 치열한 공방전을 펼쳤습니다.
>>> print(vip, "이 맹활약을 하였습니다.")
홍길동 이 맹활약을 하였습니다.
>>> print("결국", winner, "가", "loser", "를", score, "로 이겼습니다.")
결국 삼성 가 loser 를 8:7 로 이겼습니다.
>>> print("결국", winner, "이", loser, "를", score, "로 이겼습니다.")
결국 삼성 이 LG 를 8:7 로 이겼습니다.
>>> print(================================)
SyntaxError: invalid syntax
>>> print("=========================")
=========================
>>> 