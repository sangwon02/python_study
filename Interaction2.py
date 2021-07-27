from Interaction import Character #캐릭터 클래스를 불러온다.

mycharacter = Character("전사", 100) #캐릭터 두개를 생성한다.
myenemy = Character("흑마법사", 100)

while True: #한명이 죽으면 끝나도록 while구문을 짜주었다.
    mycharacter.attack(myenemy)
    mycharacter.defense(myenemy)
    if mycharacter.hp <= 0 :
        print("당신의 캐릭터가 죽었습니다. 다시하시려면 500원을 넣으십쇼.")
        break
    elif myenemy.hp <= 0:
        print("당신이 승리하였습니다.")
        break
