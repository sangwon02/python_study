items = { "커피음료": 7, "펜": 3, "종이컵": 2,
          "우유": 1, "콜라": 4, "책": 5 }
item = input("물건의 이름을 입력하시오: ");
x = int(input("새로 들어온 갯수를 입력하시오: "))
y = int(input("팔린 갯수를 입력하시오: "))
items[item] = items[item] + x - y
print ("남은 재고의 갯수:", items[item])
