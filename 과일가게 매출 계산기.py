aplle_price = 1000
grape_price = 3000
pear_price = 2000
tangerine_price = 500

aplle = int(input("사과의 판매 개수: "))
grape = int(input("포도의 판매 개수: "))
pear = int(input("배의 판매 개수: "))
tangerine = int(input("귤의 판매 개수: "))

if grape >= 3:
    sales = aplle_price*aplle
    sales = grape_price*grape + sales
    sales = pear_price*pear + sales
    sales = tangerine*tangerine_price + sales
    sales = sales*(9/10)
    print("총 가격은", sales,"입니다.")

else:
    sales = aplle_price*aplle
    sales = grape_price*grape + sales
    sales = pear_price*pear + sales
    sales = tangerine*tangerine_price + sales
    print("총 가격은", sales,"입니다.")
