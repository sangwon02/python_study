import random #랜덤과 시간을 불러온다.
import time

class Character: #캐릭터의 직업과 피를 설정할 수 있도록 만든다.
    def __init__(self, occupation, hp):
        self.occupation = occupation
        self.hp = int(hp)

    def attack(self, enemy): #공격하는 코드를 짜주었다.
        damage = random.randrange(0, 10) #0에서 10까지의 랜덤한 데미지를 준다.
        enemy.hp = enemy.hp - damage
        print("당신의 캐릭터가 %s에게 %s의 피해를 입혔습니다."%(enemy.occupation, damage))
        print("%s : %d    %s : %d" %(self.occupation, self.hp, enemy.occupation, enemy.hp))
        time.sleep(0.75) #0.75초의 딜레이를 만들어준다.
            
    def defense(self, enemy): #위에 같은 방법으로 코드를 짜준다.
        damage = random.randrange(0, 10)
        self.hp = self.hp - damage
        print("당신의 캐릭터가 %s에게 %s의 피해를 입었습니다."%(enemy.occupation, damage))
        print("%s : %d    %s : %d" %(self.occupation, self.hp, enemy.occupation, enemy.hp))
        time.sleep(0.75)
        
            
