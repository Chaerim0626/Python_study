#3장 제어문
# 1. if문
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

pocket = ['papaer', 'cellphone']
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

