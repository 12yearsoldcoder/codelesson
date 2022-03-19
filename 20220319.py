# a 5
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# b = int(input())
# c = []
# for i in a:
#     if i % b == int() or b % i == int():
#         c.append(i)
# del c[0]
# print(c)

# 6
# a = {1: 'dog', 2: 'cat', 3: 'chick'}
# b = int(input('Number? '))
# print(a[b])

# 7
# b = 0
# c = []
# while True:
#     a = int(input())
#     if a >= 100:
#         b += a
#         c.append(a)
#         break
#     b += a
#     c.append(a)
# print(b)
# d = len(c)
# e = b/d
# if str(e)[4] >= '5':
#     f = e+0.1
#     print(str(f)[:4])
# else:
#     print(str(e)[:4])

# 8

# a, b, c, d, e, f, g, h, i, j = input().split(' ')
# k = [int(a), int(b), int(c), int(d), int(e), int(f), int(g), int(h), int(i), int(j)]
# three = 0
# five = 0
# for i in k:
#     if i % 3 == 0:
#         three += 1
#     if i % 5 == 0:
#         five += 1
# print('Multiples of 3 : %d' % three)
# print('Multiples of 5 : %d' % five)

# 9 포기 난 초딩 ㅠㅠ 못해먹겠다 제곱근 에잇 던져버려
# a = float(input())
# b = float(input())
# aa = a**(1/2)
# bb = b**(1/2)
# c = abs(aa-bb)
# if (c%int(c)) >= 0.5:
#     print(int(c)+1)
# elif (c%int(c)) == 0:
#     print(int(c)-1)
# else:
#     print(int(c))

#최소공해수
# a = int(input())
# b = int(input())
# if a > b:
#     min = b
# else:
#     min = a
# for i in range(min+1,1,-1):
#     if a % 1 == 0 and b % i == 0:
#         print(i)
#         break
#최소공배수 함수 ver
def chde(x, y):
    if x < y:
        min = x
    else:
        min = y
    for i in range(min + 1, 1, -1):
        if x % i == 0 and y % 1 == 0:
            anw = i
            break
    return anw


a = int(input())
b = int(input())
print(chde(a,b))

# x = int(input())
# y = int(input())
# if a>y:
#     max = x
# else:
#     max = y
# for i in range(max,(x*y)+1):
#     if i % x == 0 and i %y == 0:
#         anw = i
#         break
