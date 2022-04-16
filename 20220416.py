# a = "Hello Python"
# a1 = "hello python"
# # print(a.find("l"))
# # print(a.index("l"))
# print(a.split())
# print(a.lower()) #이거?
# print(','.join(a1))
# a2 = "....app.le...."
# print("ㅣ", a2.lstrip("."),'ㅣ',sep="")
# print("ㅣ", a2.strip("."),'ㅣ',sep="")
# print("ㅣ", a2.rstrip("."),'ㅣ',sep="")
# a = [1,2,3,4,5]
# a = 'hello python'
# print(a[::-3]) #역순
# a[3] = 7 #수정 리스트명
# b = [2,3,4,8]
# del a[2]
# print(a)
# print(a+b)
# a = ['banana', 'cat', 'duck', 'apple']
# a.sort(reverse=False)
# print(a)
# a = ['banana', 'apple', 'cat','duck']
# print(a.index('banana'))
# # a.insert(2, 'egg')
# print(a)
# print(a.pop(2))
# print(a)
# b = [1,[2,3]]
# a.extend(b)
# print(a)

# a = ('b','d','s','a')
# print(a.count('x'))

# for i in range(10):
#     print(i)

# d = {'apple':"사과","banana" : "바나나", 3 : "삼"}
# keys = list(d.keys())
# values = list(d.values())
# items = list(d.items())
# print(keys)
# print(values)
# print(items)
# print('apple' in d.keys())

# a = [1,2,3,2,1,3,2,1,2,3,1,2,3]
# s = set(a)
# print(s)
# s1 = set([1])
# s2 = set([1,2])
# s3 = set([3,4])
# print(s1 -s2)
#
# a,b = input().split()
# if int(a[::-1]) > int(b[::-1]):
#     print(a[::-1])
# else:
#     print(b[::-1])

# a = input()
# time = 0
# for i in a:
#     if i in ['A','B','C']:
#         time += 3
#     elif i in ['D','E','F']:
#         time += 4
#     elif i in ['G','H','I']:
#         time += 5
#     elif i in ['J','K','L']:
#         time += 6
#     elif i in ['M','N','O']:
#         time += 7
#     elif i in ['P','Q','R','S']:
#         time += 8
#     elif i in ['T','U','V']:
#         time += 9
#     elif i in ['W','X','Y','Z']:
#         time += 10
# print(time)