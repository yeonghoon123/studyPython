# 함수 설명
'''
def deposit(balance, money):
    print("입금이 완료 되었습니다. 잔액은 {0}원입니다.".format(balance+money))
    return balance + money


def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료 되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance


def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission


balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
commission, balance = withdraw_night(balance, 500)
print(balance, commission)
'''

# 함수 기본값
'''
def profile(name, age=19, main_lang="파이썬"):
    print("{0}{1}{2}".format(name, age, main_lang))

profile("김영훈")
profile("andy")
'''

# 키워드 값
'''
def profile(name, age, main_lang):
    print("{0}{1}{2}".format(name, age, main_lang))
profile(age=20, name="and", main_lang="python")
profile(main_lang="java", age=31, name="ag")
'''

# 가변인자
'''
def profile(name, age, *Language):
    print(name, age, end=" ")
    for i in Language:
        print(i, end=" ")
    print()

profile("ada", 20, "C", "C++", "C#")
profile("antd", 141, "JavaScript")
'''

# 지역 변수, 전역 변수
'''
gun = 10
# 지역
def check(soliders):
    gun = 20
    gun -= soliders
    print("남은 총{0}".format(gun))
# 전역
def check_global(soliders):
    global gun
    gun = gun - soliders
    print("남은총{0}".format(gun))
# 파라미터 값 넘기기
def check_ret(gun, sol):
    gun = gun - sol
    print("남은총{0}".format(gun))
    return(gun)

check(2)
check_global(2)
gun = check_ret(gun, 2)
print(gun)
'''

# 퀴즈


def std_weight(height, gender):
    if gender == "남자":
        print("키 {0}cm의 {1}의 표준 체중은 {2}kg 입니다.".format(
            int(height*100), gender, round(height*height*22, 2)))
    if gender == "여자":
        print("키 {0}cm의 {1}의 표준 체중은 {2}kg 입니다.".format(
            height, gender, round(height*height*21, 2)))


std_weight(1.75, "여자")
