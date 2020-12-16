'''
# 리스트 []

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세오", "박명우"]
print(subway)

print(subway.index("조세오"))

# 배열 삽입
subway.append("하하")
print(subway)

# 배열 사이 삽입
subway.insert(1, "정형돈")
print(subway)

# 배열 마지막 삭제
print(subway.pop())

# 배열
subway.append("유재석")
print(subway.count("유재석"))

# 정렬
numList = [5, 14, 4, 24]
numList.sort()
print(numList)

# 오름차순
numList.reverse()
print(numList)

# 전부 삭제
numList.clear()
print(numList)

# 배열 확장
numList2 = [1, 5, 6, "Asd", 51]
numList.extend(numList2)
print(numList)
'''


# 사전
'''
cabinet = {3: "우재", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

print(cabinet.get(5, "사용가능"))
# []로 값을 받을때 없으면 에러 get으로 할경우는 none출력

print(3 in cabinet)  # true
print(5 in cabinet)  # false

cabinet = {"a-5": "우제샥", "b-5": "qrw"}

cabinet["a-3"] = "ㄱ;ㅁ종"
cabinet["c-5"] = "조시"
print(cabinet)

del cabinet["a-3"]
print(cabinet)

# key만 출력
print(cabinet.keys())

# value만 출력
print(cabinet.values())

# 둘다 출력
print(cabinet.items())

# 다 삭제
print(cabinet.clear())
'''

# 튜플
'''
menu = ["돈까스", "치즈까스"]

(name, age, hobby) = ("김정국", 20, "코딩")
print(name, age, hobby)
'''

# 세트

'''
# 집합(set)
# 중복 안됨, 순서 없음

Myset = {1, 2, 3, 3, 3}
print(Myset)

java = {"유재석", "김하", "양하"}
python = {"유재석", "asd"}

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합 둘중에 하나만 할 수있는 개발자
print(java | python)
print(java.union(python))

# 차집합 하나라도 못하는 개발자
print(java - python)
print(java.difference(python))

# python할줄 아는 사람 늘었다.

python.add("김하")
print(python)

# java를 잊음
java.remove("김하")
print(java)
'''

# 자료구조 변경
'''
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))
'''
from random import *
lst = list(range(1, 21))
shuffle(lst)
win = sample(lst, 4)
print("""
-- 당첨자 발표 --
치킨 당첨자 : %s
커피 당첨자 : %s
-- 축하 합니다--
""" % (win[0], win[1:]))
