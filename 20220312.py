# b유형

# 1
# print("1plus1 = Gwi yo mi")
# print("1 + 1 = ", 1 + 1)
#
# #2
# x = float(input("x = "))
# y = float(input("y = "))
# print(x*y)
#
# #3
# a = int(input())
# b = int(input())
# c = int(input())
# print("sum = ", a+b+c)
# print("avg = ", (a+b+c)//3)

# 4
# a = input()
# b = input()
# c = int(input())
# print(b*3+a)

# 5
# a = [1, 2]
# b = int(input())
# print(b)
# print(a[1])
# print(a[0])

# 6
# a = float(input())
# if a > 88.45:
#     print("Heavyweight")
# elif a <= 88.45:
#     print("Cruiserweight")
# elif a <= 72.57:
#     print("Middleweight")
# elif a <= 61.25:
#     print("Lightweight")
# elif a <= 50.80:
#     print("Flyweight")

# 7

# even = 0
# odd = 0
# L = []
# while True:
#     a = int(input())
#     if a == 0:
#         break
#     L.append(a)
# for i in L:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print('odd: %d' % odd)
# print('even: %d' % even)



# 8

# a,b,c,d = input().split(" ")
# e = (int(a)+int(b)+int(c)+int(d))/4
# print("avg : ",str(e)[:4])
# if e >= 80:
#     print("pass")

# 9

def nulbi():
    a = int(input())
    b = a*a*3.14
    if str(b)[5:]:
        print(b)
    else:
        print(str(b)+'0')
nulbi()

# 와 제로부터 시작하는 a유형!

# 1
# 다음과 같이 출력되는 프로그램을 작성하라. 단. 등호 = 뒤에 값은 수식을 이용해 출력하시오
# print("5 Dan")
# print('5 * 2 = ', 5*2)

# 2
# 두개의 정수를 입력받아 곱과 나눈 값을 출력하시오
# a = int(input())
# b = int(input())
# print('%d * %d = '%(a,b), a*b)
# print('%d / %d = '%(a,b), a / b)

# 3
# 실수의 야드를 입력받아 cm으로 환산한 값을 출력하는 프로그램을 작성하시오 (1야드 = 0.9144m)
# a = float(input())
# y1 = 0.9144
# print('%d yard = '%(a),a*(y1*100))

# 4
# a = input()
# b = input()
# print('%s and %s'%(a,b))
# print('%s&%s'%(a,b))
