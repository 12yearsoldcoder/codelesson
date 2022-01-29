# a = 0
# b = {3, 6, 9}
#
# while a in b:
#    print("*")
#    a += 1
#    if a not in b:
#        a += 1
#        print(a)


# a = 0
# b = [3,6,9]
# for i in range(1,101):
#    a += 1
#    if a in b:
#        print("*")
#        if a in b:
#            print("**")
# a = 0
# b = [3,6,9]
# for i in range(1,101):
#     a += 1
#     while a in b:
#         a += 1
#         while a in b:
#             print("**")
#         print("*")
#     print(a)


# for i in range(1, 101):
#     if 3 == i % 10:
#         if 6 == i // 10:
#             print("**")
#         print("*")
#         i += 1
#     print(i)
for i in range(1, 101):
    if (i // 10 == 3 or i // 10 == 6 or i // 10 == 9) and (i % 10 == 3 or i % 10 == 6 or i % 10 == 9):
        print("*")
    elif i // 10 == 3 or i // 10 == 6 or i // 10 == 9:
        print("*")
    elif i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print("**")
    else:
        print(i)
# a = 0
# while a < 100:
#     a += 1
#     if ((a%10)==3 or (a % 10) == 6 or (a%10)==9):
#         if ((a//10)==3 or (a//10)==6 or (a//10)==9):
#             print("**")
#         else:
#             print("*")
#     elif((a%10)==3 or (a % 10) == 6 or (a%10)==9):
#         print("*")
#     else:
#         print(a)