#자료형
#숫자형
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



#문자열 자료형
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
