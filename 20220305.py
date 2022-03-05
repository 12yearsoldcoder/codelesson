# def greet():
#     print("ㄴㅇㄱ ㅇㅅㅇ")

# def greet(message):#def == definition
#     print(message)
# def plus(x,y):
#     print(x+y)
# greet("Hello")
# plus(7,5)

# def minus(x,y):
#     print(x-y)
# a = 7
# b = 5
# minus(a,b)
# minus(b,a)
# minus(a+1,10//2)

# def average(x,y,z):
#     print("average=%d"%((x+y+z)/3))
# a = 7
# b = 5
# c = 9
# average(a,b,c)
# average(10,b,0)
#
# def chance(p, m):
#     print("물건 값 = %d" % (p))
#     print("받을 돈 = %d" % (m))
#     print("거스름 돈 = %d" % (m - p))
#
#
# price = int(input("물건 값? "))
# money = int(input("받은돈? "))
# chance(price, money)
#
# def welcome(n,p):
#     print("안녕하세요 %s님"%(n))
#     print("현제 %d 포인트를 보유하고 있습니다."%(p))
# name = input()
# point = int(input())
#
# welcome(name, point)

# def minus(x,y):
#     z = x-y
#     return z

# a = 7
# b = 5
# c = minus(a,b)
# minus(a,b)
# print(c)
# d = c+10
# print(d)
# if c>0:
#     print("c의 값은 양수이다.")

# def even(n):
#     return n%2 == 0
# x = int(input())
# if even(x):
#     print("짝수이다")
# else:
# #     print("홀수이다")
# def allot(sum, n):
#     return sum // n
# price = int(input())
# months = int(input())
#
# if months < 3 or months > 12:
#     print("3~13개월 할부만 가능합니다")
# else:
#     amt = allot(price,months)
#     print("월 할부금은 %d원입니다."%(amt))

# def code():
#     print("원하는 거래번호를 선택하세요")
#     print("1 입금")
#     print("2 출금")
#     print("3 취소")
#
#     code = int(input("거래번호: "))
#     return code
# c = code()
# print("%d번을 선택하셨습니다."%(c))
# if code == 1:
#     a = int(input("입금하실 계좌번호를 입력해주세요: "))


# def square(a):
#     return a**2
#
# def addsquare(a,b):
#     return square(a) + square(b)
# print("두개의 수를 입력하시오")
# x = int(input())
# y = int(input())
# print("entndml wprhqdml gkqdms %d이다"%(addsquare(x,y)))

#계산기 만들기 ㅋ
# def calculator(x, y, n):
#     if n == 1:
#         print(x+y)
#     if n == 2:
#         print(x - y)
#     if n == 3:
#         print(x * y)
#     if n == 4:
#         print(x%y)
# print("계산유형 1은 더한다")
# print("계산유형 2은 뺀다")
# print("계산유형 3은 곱한다")
# print("계산유형 4은 나눈다")
# a = int(input("1번째 숫자: "))
# b = int(input("2번째 숫자: "))
# c = int(input("계산 유형:"))
# calculator(a,b,c)

# def sum(a,b):
#     result = a+b
#     print(result)
# print(sum(4,5))
#리턴은 결과값이다.

# a = int(input())
# b = int(input())
# c = int(input())
# def finding(x,y,z):
#     if x > y and x > z:
#         print("최고값 = %d"%(x))
#     if x < y > z:
#         print("최고값 = %d"%(y))
#     if x < z > y:
#         print("최고점 = %d"%(z))
# finding(a,b,c)
#
# a = int(input())
# b = int(input())
# c = int(input())
# def finding(x,y,z):
#     if z>x<y:
#         print("최저값 = %d"%(x))
#     if x > y < z:
#         print("최저값 = %d"%(y))
#     if x > z < y:
#         print("최저값 = %d"%(z))
# finding(a,b,c)
# a = int(input())
# b = int(input())
# c = int(input())
# def just(x,y,z):
#     print((x+y+z)/3)
# just(a,b,c)

a = int(input())
b = int(input())
def yee(x,y):
    if a % b >= 0:
        c = a % b
    if b % a >= 0:
        c = b % a
