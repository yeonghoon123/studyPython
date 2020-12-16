# sentence = "네네"
# print(sentence)
# sentence2 = "asdasd"
# print(sentence2)
# sentence3 = """
# i don care
# idont know
# """
# print(sentence3)

# slice

# jumin = "020904-3163314"

# print("성별: " + jumin[7])  # 성별 : 3
# print("연: " + jumin[0: 2])  # 연 : 02  0부터 2직전 까지
# print("월: " + jumin[2: 4])  # 월 : 09  2부터 4직전 까지
# print("일: " + jumin[4: 6])  # 일 : 04  4부터 6직전 까지
# print("생년월일: " + jumin[:6])  # 생년월일 : 020904  처음부터 6직전 까지
# print("뒤 7자리: " + jumin[7:])  # 뒤 7자리 : 3163314  7부터 끝까지
# print("뒤 7자리(뒤에서 부터): " + jumin[-7:])  # 뒤 7자리 : 3163314  맨뒤에서부터 7번째 부터 끝까지

'''
# 문자열 함수
python = "Asdasd"
print(python.lower())  # 전부 소문자
print(python.upper())  # 전부 대문자
print(python[0].isupper())  # 대문자 판단
print(len(python))  # 문장의 길이
print(python.replace("asd", "dsa"))  # 문장 바꾸기

index = python.index("d")
print(index)  # d가 들어가는 문장 순서 구하기
index = python.index("d", index+1)
print(index)  # d가 들어가는 문장에 순서와 그 다음에 또 나올 경우에 나오는 값

print(python.find("Asd"))  # 없을 경우 -1출력 있을때 0 출력
print(python.index("asd"))  # 없을 경우 에러 출력

print(python.count("d"))  # d의 개수 구하기
'''

# 문자를 합치는 법
# 첫번째 방법
print("나는 %d살입니다." % 19)
