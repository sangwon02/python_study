Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> money=int(input("투입한 돈:"))
투입한 돈:5000
>>> price=int(input("물건 값:"))
물건 값:2600
>>> change=money-price
>>> print(" 거스름돈:", change)
 거스름돈: 2400
>>> coin500s=change//500
>>> change=change%500
>>> coin100s=change//100
>>> print("500원의 동전의 개수", coin500s)
500원의 동전의 개수 4
>>> print("100원의 동전의 개수", coin100s)
100원의 동전의 개수 4
>>> 