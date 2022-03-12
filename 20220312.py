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

# b = []
# d = 0
# e = 0
# while True:
#     a = int(input())
#     if a == 0:
#         break
#     b.append(a)
# for i in b:
#     if i // 2 == 0:
#         d += 1
#     else:
#         e += 1
# print('odd : ',e)
# print('even : ',d)
# 짝수의 조건 = 나누기 2를 하면 소수점 없는 값이 나오는것


# 8
'''
a,b,c,d = input().split(" ")
e = (int(a)+int(b)+int(c)+int(d))/4
print("avg : ",str(e)[:4])
if e >= 80:
    print("pass")
'''

# 9
'''
def nulbi():
    a = int(input())
    b = a*a*3.14
    if str(b)[5:]:
        print(b)
    else:
        print(str(b)+'0')
nulbi()
'''

# 와 제로부터 시작하는 a유형!

# 1
# print("5 Dan")
# print('5 * 2 = ', 5*2)

# 2
# a = int(input())
# b = int(input())
# print('%d * %d = '%(a,b), a*b)
# print('%d / %d = '%(a,b), a / b)

# 3
# a = float(input())
# y1 = 0.9144
# print('%d yard = '%(a),a*(y1*100))

# 4
# a = input()
# b = input()
# print('%s and %s'%(a,b))
# print('%s&%s'%(a,b))

# 5
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
b = int(input())
for i in a:
    if i%3 == type(int):
        print(i)
