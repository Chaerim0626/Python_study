#불 대수 : 일상적인 논리를 수학적으로 표현한 것
#불 대수 연산 : AND, OR, NOT

#AND 연산 : X AND y에서 x,y가 모두 참이어야 참
#OR 연산 : X OR y에서 x,y 중 하나가 참이면 참
#NOT 연산 : NOT x, x가 아니면 참

# 불린 (Boolean) : True, False
print(True and True) #True
print(False and False) #False
print(True or False) #True
print(2 != 2) #False
print(2 == 2) #True
print(2 > 1 and "Hello" == "Hello") #True
print(not not True) #True

#type 함수 : 어떤 자료형인지 확인
print(type("3")) #str
print(type(3)) #int
print(type(3.0)) #float
print(type(True)) #bool
print(type("True")) #str