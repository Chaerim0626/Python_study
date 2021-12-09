#자료형
#1. 숫자형
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



#2. 문자열 자료형
say = "\"Python is very easy.\" he says." #큰따옴표, 작은따옴표를 문자로 쓰고 싶을때는 앞에 백슬래쉬 쓰기

#개행 ('''나 """)
multiline = ''' 
Life is too short
You need python
'''
print(multiline)

head = "head"
tail = "tail"
head+tail #문자열 더해서 연결
temp = head * 2 #문자열 곱하기
temp2 = head[3] #문자열 인덱싱
temp3 = tail[0:4] #0부터 3까지 문자열 슬라이싱

date = "20211115" #슬라이싱으로 문자열 나누기
year = date[:4]
day = date[4:]

#문자열 포맷팅
temp4 = "I eat %d apples." %3  #1.숫자바로대입
print(temp4)

temp5 = "I eat %s apples." % "five" #2.문자열 바로 대입

number = 10
day = "three"
temp6 = "I ate %d apples. so I was sick for %s days." %(number,day) #3. 2개이상의 값 넣기
print(temp6)

word = "hobby"
word.count('b') #문자세기 함수
word.find('b') #문자찾기 함수
word.find('k')
word.index('h') #문자찾기 함수
word.join(" abcd") #문자열 삽입 함수
word.upper() #소문자->대문자
word.lower() #대문자->소문자
word.lstrip() #왼쪽 공백 지우기
word.rstrip() #오른쪽 공백 지우기
word.strip() #양쪽 공백 지우기
word.replace("h", "o") #문자열 바꾸기
word.split() #문자열 공백기준으로 나누기

#고급 문자열 포맷팅
print("I eat {0} apples.".format(3)) #숫자 바로 대입하기
print("I eat {0} apples.".format("five")) #문자열 바로 대입하기
number = 3
print("I eat {0} apples.".format(number)) #숫자값을 가진 변수로 대입하기
day = "five"
print("I ate {0} apples. so I was sick for {1} days.".format(number,day)) #2개이상의 값 넣기


#3. 리스트 자료형
odd = [1, 3, 5, 7, 9] #리스트 형식
a = [1, 2, 3, 4, 5]
print(a[0:2]) #리스트 슬라이싱은 문자열 슬라이싱과 동일
print(odd + a) #리스트 더하기
print(a*3) #리스트 반복하기

#리스트의 수정, 변경, 삭제
a[2] = 4
a[1:2] = ['a', 'b', 'c']
a[1:3] = []
del a[1]

#리스트 관련 함수들
b = [1, 2, 3]
b.append([4, 5]) #리스트 마지막에 추가
b.reverse() #리스트 뒤집기
b.index(1) #위치 반환
b.insert(0,4) #리스트에 요소 삽입
b.remove(1) #첫번째로 나오는 1을 제거
b.pop() #리스트의 맨 마지막 요소 꺼내 삭제
b.pop(1) #리스트의 1번째 요소 꺼내 삭제
b.count(2) #리스트에 2가 몇개 있는지 세기
b.sort() #리스트 정렬
c = [6,7]
b.extend(c) #b에 c리스트 더하기
print(b)


#4. 튜플 자료형
#리스트는 그 값의 생성, 삭제, 수정 가능 but 튜플은 그 값을 바꿀 수 없음
t1 = (1, 2, 3, 4)
t1[0] #튜플 인덱싱
t1[1:] #튜플 슬라이싱
t1 * 3 #튜플 곱하기

#5. 딕셔너리 자료형

d1 = {1: 'hi'} #key는 1, value는 hi
#key에는 list형은 쓸 수 없음
d1[2] = 'b' #딕셔너리 쌍 추가
del d1[2] #key가 2인 딕셔너리 요소 삭제하기
d1[1] #key가 1인 value값 얻기

a = {'name': 'pey', 'phone': '01022222222', 'birth': 1118}
a.keys() #key 리스트 만들기
for k in a.keys():
    print(k)
list(a.keys()) #dict_keys 객체를 리스트로 변환
a.values() #value 리스트 만들기
a.clear() #모두 삭제
a.get('name') #key로 value 얻기
print('name' in a) #딕셔너리 안에 해당 key가 있는지 조사

#6. 집합 자료형