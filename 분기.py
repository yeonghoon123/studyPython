# if
'''
weather = input("오늘 날씨는 어때요")
if weather == "비" or weater == "눈":
    print("우산을 챙겨요")
elif weather == "미세먼지":
    print("마스크를 써요")
else:
    print("준비물 필요 없어요")

temp = int(input("기온이 어때요"))
if temp >= 30:
    print("너무 더워요")
elif 10 <= temp and 30 < temp:
    print("적당해요")
elif 0 <= temp and temp < 10:
    print("외투를 챙겨요")
else:
    print("얼어죽으니 나가지 마요")
'''

# for
'''
# for watting in range(1, 6):
#     print("대기번호: {0}".format(watting))

star = ["asd", "asdas", "asdasd", "agag"]
for count in star:
    print("{0}번 손님 음식 나옴".format(count))
'''

# while
'''
# cus = "xhs"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다..{1}번 남았슴".format(cus, index))
#     index -= 1
#     if index == 0:
#         print("커피 버림")

# cus = "아이"
# i = 1
# while True:
#     print("{0}, 커피가 준비 되었어요! {1}불렀어요.".format(cus, i))
#     i += 1
#     if i > 100:
#         break

cus = "토르"
per = "unknown"

while per != cus:
    print("%s님 음식 나왔어요." % cus)
    per = input("이름이 어떻게 되세요.")
'''

# coutinue, break
'''
absent = [2, 5]
nob = [8]
for std in range(1, 11):
    if std in absent:
        continue
    elif std in nob:
        print("오늘은 여기까지 %s번은 교모실로" % std)
        break
    print("%s번 책좀 읽어" % std)
'''

# for 한줄
'''
student = [1, 2, 3, 4, 5]
student = [i+100 for i in student]
print(student)
student = ["Asdasd", "Asgasdashasd", "Asdasdasd"]
student = [len(i) for i in student]
print(student)
student = ["Asdasd", "Asgasdashasd", "Asdasdasd"]
student = [i.upper() for i in student]
print(student)
'''

# 퀴즈

from random import *
time = [randint(5, 50) for i in range(1, 51)]
stair = 0
use = 0

for i in time:
    stair += 1
    if i <= 15 and i >= 5:
        print("[O]" + str(stair) + "번째 손님 (소요시간 : "+str(i)+"분)")
        use += 1
    else:
        print("[ ]" + str(stair) + "번째 손님 (소요시간 : "+str(i)+"분)")

print("총 탑승 승객 :"+str(use)+"분")
