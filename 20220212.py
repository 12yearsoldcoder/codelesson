# a = ['a','b','c','d']
# b = ['e','f']
# print(a+b)
# print((a+b)*3)
# a = [4, 1, 3, 2, 5]
# print(a)
# print(a)
# a.reverse()
# print(a)
# a.reverse()
# print(a)
# a.reverse()
# a = [4, 1, 3, 2]
# # print(a.index(7)) #= ValueError
# # a.insert(0,6) #0번째의 6 넣음
# # print(a)
# # a.remove(4)
# print(a)
# print(a.pop(), a)
#
# print(a.count(4))
# a = (4,1,3,2,4) #수정 불가
# #b = [5,7]
# # a.append(b)
# # print(a)
# # a.extend(b) #[]안들어감 걍 확장임
# # print(a)
# # a[2] = 9 #튜플이 안수정이 되는데 하려는 그는 도덕책...
# # print(a)
# # del a[2]
# 나머지는 리스트랑 같음
# print(len(a))
# 딕셔너리 {} 키값
# 예: d = {'apple':'사과','banana':'바나나}
# d = {"apple": "사과", "banana": "바나나", 3: "삼", 4: '사'}
# print(d)
# del d[4]
# print(d)
# 과자 = 'snack'
# print(과자)
# print(d['banana'])
# key = d.keys()
# value = d.values()
# item = d.items()
# print(key)
# print(value)
# print(item)
# print("Mary's cosmetics")
# print("오늘은","토요일")
# 삼성 = 50000 #바인딩
# print(삼성 * 10,'dnjs')
# 시가총액 = 290000000000000
# 현재가 = 50000
# PER = 15.09
# print(시가총액, type(시가총액))
# print(현재가, type(현재가))
# print(PER, type(PER))
# s = 'hello'
# t = 'python'
# print(s+"!",t)
# letters = 'python'
# print(letters[0], letters[2])
# license_plate = "24가 2210"
# print(license_plate[4:8])  # -수는 뒤부터 1234에유
# string = "홀짝홀짝홀짝"
# print(string[1::2])
# string = "python"
# print(string[::-1])
# phone_number = "010-1111-2222"
# print(phone_number.replace('-',' '))
# string = 'abcdfe2a354a32a'
# print(string.replace())
# t1 = 'python'
# t2 = 'java'
# print((t1+" "+t2+" ")*4)
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print("이름: %s 나이: %d" % (name1, age1))
#
# print("이름: %s 나이: %d" % (name2, age2)) #% = 포메팅 ㅇ기에선 "{}{}"하고 끝에 .format ()하면됨 ㅇㅇ {1},{0}으로 순서 ㅆㄱㄴ
# print("이름:",name1,"나이:",age1)
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print(f"이름: {name1} 나이: {age1}")
# print(f"이름: {name2} 나이: {age2}")
# 상장주식수 = "5,969,782,550"
# 컴마제거 = 상장주식수.replace(",", "")
# 타입변환 = int(컴마제거)
# print(타입변환, type(타입변환))
# data = "....삼성.전자...."
# print(bool())
# a = int(input("입력값:"))
# if a + 20 <= 255:
#     print(a + 20)
# else:
#     print(225)
# a = int(input("입력값:"))
# if a - 20 >= 0:
#     print(a-20)
# else:
#     print(0)
# fruit = ["사과", "포도", "홍시"]
# a = str(input())
# if a in fruit:
#     print("정답입니다!")
# else:
#     print("오답입니다!")
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# a = input("내가 좋아하는 과일은:")
# if a in fruit.values():
#     print("정답입니다")
# else:
#     print("오답입니다")
# b = 0
# for i in range(3):
#     b += 10
#     print(b)
for i in range(30):
    if i % 3 == 0:
        print(i)