#2장 자료형
#2-1 숫자형
a = 123
a = 1.2
a = 0o177 #8진수 (0o or 0O로 시작)
b = 0xABC #16진수 (0x로 시작)
a = 1+2j #복소수 (i대신 j를 사용)
a.real #실수부분
a.imag #허수부분
a.conjugate() #켤레복소수
abs(a) #a의 절댓값

c = 3
d = 4
print (c ** d) #제곱 연산자

7 % 3 #나머지 연산자
7 // 4 #소수점 아랫자리 버리는 연산자



#2-2 문자열 자료형
say = "\"Python is very easy.\" he says." #큰따옴표, 작은따옴표를 문자로 쓰고 싶을때는 앞에 백슬래쉬 쓰기

#개행 ('''나 """)
multiline = ''' 
Life is too short
You need python
''' #"""사용해도됨
print(multiline)

head = "head"
tail = "tail"
head+tail #문자열 더해서 연결
temp = head * 2 #문자열 곱하기
len(temp) #문자열 길이 구하기
temp2 = head[3] #문자열 인덱싱
temp3 = tail[0:4] #0부터 3까지 문자열 슬라이싱
temp31 = head[-2] #뒤에서 2번째 문자 인덱싱

#슬라이싱으로 문자열 나누기
date = "20211115"
year = date[:4] #시작부터 3까지
day = date[4:] #3부터 끝까지

#문자열 포맷팅
temp4 = "I eat %d apples." %3  #1.숫자바로대입
print(temp4)

temp5 = "I eat %s apples." % "five" #2.문자열 바로 대입

number = 10
day = "three"
temp6 = "I ate %d apples. so I was sick for %s days." %(number,day) #3. 2개이상의 값 넣기
print(temp6)

#포맷 코드와 숫자 함께 사용하기
temp7 = "%10s" % "hi" #오른쪽 정렬
temp8 = "%-10sjane" % "hi" #왼쪽정렬
print(temp7)
print(temp8)

temp9 = "%0.4f" % 3.4121334432 #소수점 네 번째 자리까지 표시
print(temp9)

#format 함수를 사용한 포매팅
print("I eat {0} apples.".format(3)) #숫자 바로 대입하기
print("I eat {0} apples.".format("five")) #문자열 바로 대입하기
number = 3
print("I eat {0} apples.".format(number)) #숫자값을 가진 변수로 대입하기
day = "five"
print("I ate {0} apples. so I was sick for {1} days.".format(number,day)) #2개이상의 값 넣기
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)) #이름으로 넣기

print("{0:<10}".format("hi")) #왼쪽 정렬
print("{0:>10}".format("hi")) #오른쪽 정렬
print("{0:=^10}".format("hi")) #가운데 정렬 및 공백 채우기
print("{0:0.4f}".format(3.234234)) #소수점 표현하기
print("{{ and }}".format()) # {} 문자 표현하기

# f문자열 포맷팅
name = "홍길동"
age = 30
print(f"나의 이름은 {name}이고, 나이는 {age}입니다.")


word = "hobby"
word.count('b') #문자세기 함수
word.find('b') #문자찾기 함수
word.find('k') #없으므로 -1반환
word.index('h') #문자찾기 함수, 없으면 오류 발생
word.join("abcd") #문자열 삽입 함수, abcd사이에 hobby 삽입
word.upper() #소문자->대문자
word.lower() #대문자->소문자
word.lstrip() #왼쪽 공백 지우기
word.rstrip() #오른쪽 공백 지우기
word.strip() #양쪽 공백 지우기
word.replace("h", "o") #문자열 바꾸기
word.split() #문자열 공백기준으로 나누기


#2-3 리스트 자료형
odd = [1, 3, 5, 7, 9] #리스트 형식
a = [1, 2, 3, 4, 5]
print(a[0]) #리스트 인덱싱은 문자열 인덱싱과 동일
print(a[0:2]) #리스트 슬라이싱은 문자열 슬라이싱과 동일
print(odd + a) #리스트 더하기
print(a*3) #리스트 반복하기
print(len(a)) #리스트 길이 구하기

#리스트의 수정, 변경, 삭제
a[2] = 4
a[1:2] = ['a', 'b', 'c']
del a[0]
print(a)

#리스트 관련 함수들
b = [1, 2, 3]
b.append([4, 5]) #리스트 마지막에 추가
b.reverse() #리스트 뒤집기
b.index(1) #위치 반환
b.insert(0,4) #리스트에 요소 삽입, 0위치에 4삽입
b.remove(1) #첫번째로 나오는 1을 제거
b.pop() #리스트의 맨 마지막 요소 꺼내 삭제
b.pop(1) #리스트의 1번째 요소 꺼내 삭제
b.count(2) #리스트에 2가 몇개 있는지 세기
b.sort() #리스트 정렬
c = [6,7]
b.extend(c) #b에 c리스트 더하기
print(b)


#2-4 튜플 자료형
#리스트는 그 값의 생성, 삭제, 수정 가능 but 튜플은 그 값을 바꿀 수 없음
t1 = (1, 2, 3)
t1[0] #튜플 인덱싱
t1[1:] #튜플 슬라이싱
t1 * 3 #튜플 곱하기
len(t1) #튜플 길이 구하기
t2 = t1 + (4,)
print(t2)


#2-5 딕셔너리 자료형
d1 = {1: 'hi'} #key는 1, value는 hi
#key에는 list형은 쓸 수 없음
d1[2] = 'b' #딕셔너리 쌍 추가
del d1[2] #key가 2인 딕셔너리 요소 삭제하기
d1[1] #key가 1인 value값 얻기

#딕셔너리 관련 함수
a = {'name': 'pey', 'phone': '01022222222', 'birth': 1118}
a.keys() #key 리스트 만들기, 객체임
for k in a.keys():
    print(k)
list(a.keys()) #dict_keys 객체를 리스트로 변환
a.values() #value 리스트 만들기
a.items() #Key, Value 쌍 얻기
a.clear() #모두 삭제
a.get('name') #key로 value 얻기
print('name' in a) #딕셔너리 안에 해당 key가 있는지 조사


#2-6 집합 자료형
s1 = set([1, 2, 3])
print(s1)
s11 = set("Hello") #집합자료형은 set()안에 리스트를 입력하거나 문자열을 입력해 만들 수 있음

#중복 허용 X, 순서 X
#딕셔너리와 집합 모두 순서가 없는 자료형이라 인덱싱 지원X
l1 = list(s1) #리스트로 자료형 변환
t1 = tuple(s1) #튜플로 자료형 변환
s2 = set([3, 4, 5, 6])
print(s1 & s2) #교집합 구하기
print(s1.intersection(s2)) #교집합 구하기
print(s1 | s2) #합집합 구하기
print(s1.union(s2)) #합집합 구하기
print(s1 - s2) #차집합 구하기
print(s1.difference((s2))) #차집합 구하기
s1.add(4) #값 1개 추가
s1.update([5, 6]) #값 여러개 추가
s1.remove(6) #특정 값 제거
print(s1)


#2-7 불자료형
#문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어있으면 거짓이 됨
if []:
    print("True")
else:
    print("False")
bool("python") #True
bool("") #False

#2-8 자료형의 값을 저장하는 공간 : 변수
#변수명 = 변수에 저장할 값
a = 3 #3은 상수가 아닌 정수형 객체

a = [1, 2, 3]
b = a #리스트 복사, a와 b는 같은 주소를 가리킴
b = a[:] #리스트 처음요소부터 끝 요소까지 슬라이싱 해 복사, a와는 다른 주소 가리킴

from copy import copy #copy 모듈 사용
b = copy(a) #a와 b는 다른 주소 가리킴
print (b is a) #false

#변수를 만드는 여러 가지 방법
a, b = ('python', 'life')
[a,b] = ['python', 'life']
a = b = 'python'
c = 3
d = 5
c, d = d, c
del(c) #특정한 객체를 가리키는 변수 없애기 (메모리에서 삭제)



#2장 연습문제
#1
kor = 80
eng = 75
math = 55
avg = (kor+eng+math)/3
print(avg)

#2
if (13%2) == 0:
    print("짝수")
else:
    print("홀수")

#3
pin = "881120-1068234"
yyyymmdd = pin[:6]
print(yyyymmdd)
num = pin[7:]
print(num)

#4
print(pin[7])

#5
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

#6
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

#7
a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print(result)

#8
a = (1, 2, 3)
a += (4,)
print(a)

#9 : 딕셔너리 key로는 변하는 값을 사용할 수 없음

#10
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

#11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

#12
a = b = [1, 2, 3]
a[1] = 4
print(b) #a, b는 동일한 list 객체를 가리키고 있어 b[1]의 값도 변경됨

