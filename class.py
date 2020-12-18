from random import *
# 마린 : 공격유닛, 군인. 총을 쏨
'''
name = "마린"
hp = 40
damage = 5

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크 : 공격, 탱크. 포를 쏘고 일반/시즈
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))


def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]".format(
        name, location, damage))


attack(name, "2시", damage)
'''

# class 연습 init,멤버 변수


# marine1 = Unit("마린", 40, 15)
# tank = Unit("탱크", 150, 35)

# tank1 = Unit("시즈모드 탱크", 150, 35)
# tank1.siz = True

# if tank1.siz == True:
#     print("시즈모드변환{0}유닛".format(tank1.name))


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} : 유닛이 생성되었습니다.".format(name))

    def damaged(self, damage):
        if self.hp > 0:
            print("{0} : {1}만큼 공격받았습니다!".format(self.name, damage))
            self.hp -= damage
            print("{0} : 남은 체력은 {1}".format(self.name, self.hp))
            if self.hp <= 0:
                print("유닛이 파괴되었습니다")
        else:
            print("{0} : 유닛은 이미 파괴 되어 사용할수 없습니다.")

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1}시 방향으로 이동 중입니다.[속도 : {2}".format(
            self.name, location, self.speed))


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1}시방향으로 적군을 공격했습니다.".format(self.name, location))


class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 50, 5, 1)

    def steamPack(self):
        if self.hp <= 10:
            print("{0} : 체력이 부족하여 스팀팩사용에 실패했습니다.".format(self.name))
        else:
            print("{0} : 스팀팩을 사용합니다.".format(self.name))
            self.hp -= 10


class Tank(AttackUnit):
    sizModeDev = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 100, 3, 10)
        self.sizMode = False

    def setSizMode(self):

        if Tank.sizModeDev == False:
            return

        if self.sizMode == True:
            print("{0} : 시즈모드로 바뀌어 데미지가 증가합니다.".format(self.name))
            self.damage *= 2
            self.sizMode = False
        else:
            print("{0} : 시즈모드가 헤제되어 데미지가 감소합니다.".format(self.name))
            self.damage /= 2
            self.sizMode = True


# 날수있는 유닛


class FlyUnit:
    def __init__(self, fly_speed):
        self.fly_speed = fly_speed

    def fly(self, name, location):
        print("{0} : {1}시방향으로 날아 갑니다.[속도 :{2}]"
              .format(name, location, self.fly_speed))

# 날면서 공격하는 유닛


class FlyAttackUnit(AttackUnit, FlyUnit):
    def __init__(self, name, hp, damage,  fly_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        FlyUnit.__init__(self, fly_speed)

    def move(self, location):
        print("[비행 유닛 이동중]")
        self.fly(self.name, location)


class Wraith(FlyAttackUnit):

    def __init__(self):
        FlyAttackUnit.__init__(self, "레이스", 70, 6, 5)
        self.cloking = False

    def setCloking(self):
        if self.cloking == True:
            print("{0} : 클로킹 모드로 변환되어 상대가 보이지 않습니다.".format(self.name))
            self.cloking = False
        else:
            print("{0} : 클로킹 모드가 헤제되어 상대에게 보입니다..".format(self.name))
            self.cloking = True


def gameStart():
    print("게임 시작합니다")


def gameOver():
    print("[Player] : GG ")


# 게임시작
gameStart()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t1 = Tank()

w1 = Wraith()

attack_unit = []
attack_unit.append(m1)
attack_unit.append(m2)
attack_unit.append(m3)
attack_unit.append(t1)
attack_unit.append(t1)
attack_unit.append(w1)

for unit in attack_unit:
    unit.move(1)

Tank.sizModeDev = True
print("탱크 시즈모드 개발 완료")

for unit in attack_unit:
    if isinstance(unit, Marine):
        unit.steamPack()
    elif isinstance(unit, Tank):
        unit.setSizMode()
    elif isinstance(unit, Wraith):
        unit.setCloking()

for unit in attack_unit:
    unit.attack(1)

for unit in attack_unit:
    unit.damaged(randint(5, 21))


for unit in attack_unit:
    unit.damaged(randint(5, 21))

for unit in attack_unit:
    unit.damaged(randint(5, 21))


for unit in attack_unit:
    unit.damaged(randint(5, 21))
for unit in attack_unit:
    unit.damaged(randint(5, 21))
gameOver()
