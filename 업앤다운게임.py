from random import *


class AnswerError(Exception):
    pass


count = 0
try:
    자리수 = int(input("최대 몇까지 하고 싶습니까?(숫자만 입력하세요.)\n"))
    if 자리수 <= 0:
        raise ValueError
    print("1부터 {0}까지중 랜덤으로 숫자하나를 뽑겠습니다.\n".format(자리수))
    정답 = randint(1, 자리수)
    while True:
        대답 = int(
            input("[1 ~ {0}]정답이라고 생각하는 수를 입력하세요.(숫자로 입력하세요)\n".format(자리수)))
        if 대답 <= 0 or 대답 > 자리수:
            raise ValueError
        if 대답 > 정답:
            print("DOWN!! [입력하신 수: {0}]\n".format(대답))
            count += 1
        elif 대답 < 정답:
            print("UP!! [입력하신 수: {0}]\n".format(대답))
            count += 1
        else:
            print("정답입니다. 정답은 : {0}이였습니다.".format(정답))
            count += 1
            print("총 {0}번 만에 정답을 맞추었습니다.".format(count))
            break

except ValueError:
    print("잘못 입력하였습니다.")
