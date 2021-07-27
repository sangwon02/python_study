friend_list = [ ]

while True :
    friend = input("친구를 입력하시오(멈추려면: 그만): ")
    friend_list.append(friend)
    if friend == '그만':
        break
friend_list.remove('그만')
print("당신의 친구는", friend_list, "입니까?")
