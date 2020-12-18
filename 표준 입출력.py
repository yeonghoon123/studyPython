# 입출력
'''
import sys
print("python", "habea", file=sys.stdout)
print("python", "habea", file=sys.stderr)
'''

# 출력
'''
scores = {"수힉": 0, "영어": 13, "코딩": 100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")
'''

# 은행 대기 순번표
'''
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))
'''

# 입력
'''
answer = input("아무값이나 입력")
print("입력하신 값은 {0}입니다.".format(answer))
'''

# 다양한 출력 포맷
'''
print("{0: >10}".format(500))
# 양수 일떈 +로 표시 , 음수일때 -로 표식
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬, 빈칸은 _로 채움
print("{0:_<+10}".format(500))
# 3자리 마다 콤머 찍어주기
print("{0:,}".format(1000000000))
print("{0:+,}".format(1000000000))
print("{0:+,}".format(-1000000000))
# 3자리 마다 콤마, 부호, 자릿수, 빈자르는 ^
print("{0:^<+30,}".format(10000000000000))
# 소수점
print("{0:f}".format(5/3))
# 소수점 특정자리수 만큼
print("{0:.2f}".format(5/3))
'''
# 파일 입출력
'''
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 15", file=score_file)
score_file.close
'''
'''
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 100")
score_file.write("\n코딩 : 100")
score_file.close
'''
'''
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close
'''
'''
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close
'''
'''
score_file = open("score.txt", "r", encoding="utf8")
line = score_file.readlines()
for line in line:
    print(line, end="")
score_file.close
'''
# pickle
'''
profile_file = open("profile.pickle", "wb")
profile = {"이름": "박명수", "직업": "개그맨", "취미": ["게임", "코딩", "축구"]}
print(profile)
pickle.dump(profile, profile_file)
profile_file.close
'''
'''
profile_file = open("profile.txt", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close
'''

# with

'''
with open("profile.pickle", "rb")as profile_file:
    print(pickle.load(profile_file))
'''
'''
with open("stduy.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬 공부 하는중")
'''
'''
with open("stduy.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
'''

# 퀴즈
for i in range(1, 6):
    with open("{0}주차.txt".format(i), "w", encoding="utf8") as txt_file:
        txt_file.write("-{0}주차 주간보고 -\n".format(i))
        txt_file.write("부서 :\n")
        txt_file.write("이름 :\n")
        txt_file.write("업무 요약 :")
