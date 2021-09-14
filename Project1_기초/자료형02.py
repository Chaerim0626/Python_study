# 2.문자열
print("Hello World")
print('Hello World')

# 문자열 더하기 연산 = 문자연결
print("Hello" + "World")
print("3" + "5") #문자열 35가 출력

# \' \"
print("Hello \'world\'")

#형변환 (Type casting)
print(int(3.8)) #정수형변환 -> 3으로 출력
print(float(3)) #실수형변환 -> 3.0으로 출력
print(int("2") + int("5")) #정수형 변환 2+5 = 7출력
print(str(2)+ str(5)) #문자열 변환 2+5 = 25출력

#str과 int형을 연결시킬 수 없음
age = 24
print("제 나이는 " + str(age) + "살 입니다.")

#문자열 포맷팅 다루기
year = 2021
month = 7
day = 4
print("오늘은 {}년 {}월 {}일 입니다.".format(year,month,day))

print("저는 {1},{0}를 좋아합니다.".format("사과","복숭아"))

#소수둘째자리까지만 나타내기
num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1,num_2,num_1/num_2))

#문자열 포맷팅 오래된 방식 (%기호) (c언어, 자바 등)
age = 24
print("나이는 %d살입니다." %(age))

#f-string 방식
age = 24
print(f"나이는 {age}살입니다.")