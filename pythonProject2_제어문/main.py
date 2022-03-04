#3장 제어문
# 3-1 if문
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# x in s, x not in s
print(1 in [1, 2, 3]) #True
print(4 in [1, 2, 3]) #False

money2 = True
if money2:
    pass
else :
    print("걸어가라")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시 타고 가라")
elif card:
    print("택시 타고 가라")
else:
    print("걸어 가라")

#조건부 표현식
score = 80
if score >= 60:
    message = "success"
else:
    message = "failure"

message = "success" if score >= 60 else "failure"
#조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우


#3-2 while문

#while문 빠져나가기 : break
coffee = 10
while True:
    money = int(input("돈을 넣어주세요 : "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee - 1
    elif money > 300 :
        print("거스름돈 %d원을 주고 커피를 줍니다." %(money - 300))
        coffee = coffee - 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." %coffee)

    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

#while문 맨 처음으로 돌아가기
a = 0
while a < 10:
    a = a+1
    if a % 2 == 0: continue
    print(a)

#3-3 for문

#전형적인 for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

#다양한 for문
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

#range함수
add = 0
for i in range(1, 11):
    add = add + i
print(add)

for i in range(2,10):
    for j in range(1,10):
        print(i*j, end="")
    print(' ')

#리스트 내포하기
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)

result2 = [num*3 for num in a]
print(result)

#리스트 내포 : 표현식 for 항목 in 반복 가능 객체 if 조건

#3장 연습문제



