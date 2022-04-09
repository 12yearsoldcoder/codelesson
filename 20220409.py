# 1. read  사용하는 경우
# MyFile = open('practice.txt','r')
# print(MyFile.read().count("\n")+1)
# MyFile.close()

# 2. readline() 쓰는 경우
# 읽어들일 값이 없을때까지 count를 매번 해야됨
# MyFile = open('practice.txt','r')
# cnt = 0
# while True:
#     if MyFile.readline() == '':
#         break
#     cnt += 1
# print(cnt)
# MyFile.close()

# 3. readlines()
# MyFile = open('practice.txt','r')
# print(len(MyFile.readlines()))
# MyFile.close()


# a, b = input().split(",")
#
#
# def star(a, b):
#     c = int(a)
#     d = int(b)
#     if c > d:
#         for j in range(d, c + 1):
#             print("== %d dan ==" % j)
#             for i in range(1, 10):
#                 print("%d * %d = %d" % (j, i, j * i))
#     else:
#         for j in range(c, d + 1):
#             print("== %d dan ==" % j)
#             for i in range(1, 10):
#                 print("%d * %d = %d" % (j, i, j * i))
#
#
# star(a, b)

# a = ['first','second','third']
# def golbengi():
#     print('@'*10)
# for i in a:
#     print(i)
#     golbengi()

# 1 2 3
# 2 4 6
# 3 6 9
def square(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i*j, end="  ")
        print()
n = int(input())
square(n)