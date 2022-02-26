# #오늘도 ㄱㅈㅇ!!
# villagernumber, villagernumberend = input().split('-')
# b = villagernumberend[1:3]
# c = int(b)
#
# if 0 <= c <= 8:
#     print("서울주민입니다.")
# else:
#     print("서울주민이 아닙니다.")

# a, b = input().split('-')
# c = int(a[0])*2+int(a[1])*3+int(a[2])*4+int(a[3])*5+int(a[4])*6+int(a[5])*7
# d = int(b[0])*8+int(b[1])*9+int(b[2])*2+int(b[3])*3+int(b[4])*4+int(b[5])*5
# e = (c+d) % 11
# f = 11 - e
# if int(b[6]) == f:
#     print("유효한 주민등록번호입니다.")
# else:
#     print("유효하지 않은 주민등록번호입니다.")


# for i in range(3):
#     a = int(input())
#     print(a)

# a = 0
# for i in range(3):
#     a += 10
#     print(a)

# L = [100,200,300]
# for i in range(3):
#     bugasae = 10
#     print(L[i] + bugasae)

# L = ["김밥", "라면", "튀김"]
# for i in range(3):
#     print("오늘의 메뉴는:",L[i])

# L = ["SK하이닉스", "삼성전자", "LG전자"]
# for i in range(3):
#     print(len(L[i]))

# L = ['dog', 'cat', 'parrot']
# for i in range(3):
#     print(L[i], len(L[1]))

# L = ['dog', 'cat', 'parrot']
# for i in range(3):
#     a = L[i]
#     print(a[0])

# L = [1, 2, 3]
# for i in range(3):
#     print("3 x", L[i])

# L = [1, 2, 3]
# for i in range(3):
#     print("3 x %d =".format(L[1]), 3 * L[i])

# L = ["가", "나", "다", "라"]
# for i in range(3):
#     print(L[i+1])

# L = ["가", "나", "다", "라"]
# for i in L[::2]:
#     print(i)

# L = ["가", "나", "다", "라"]
# for i in L[::-1]:
#     print(i)

# 리스트 = [3, -20, -3, 44]
# for a in 리스트:
#     if a<0:
#         print(a)

# 리스트 = [3, 100, 23, 44]
# for i in 리스트:
#     if i % 23 == 0:
#         print(리스트)

리스트 = [13, 21, 12, 14, 30, 18]
for i in 리스트:
    if (i < 20 and (i % 3 == 0)):
        print(i)