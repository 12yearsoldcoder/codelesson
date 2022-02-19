# str = input()
# print(str*2)

# integer = int(input())
# print(integer + 10)

# integer = int(input())
# if integer % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# integer = int(input("수를 입력하세요: "))
# if integer + 20 <= 225:
#     print(integer + 20)
# else:
#     print(255)

# integer = int(input())
# if integer - 20 <= 255 and integer - 20 >= 0:
#     print(integer - 20)
# elif integer - 20 >= 255:
#     print(255)
# else:
#     print(0)

# anyth = input()
# if anyth[3:5] == "00":
#     print("정각입니다")
# else:
#     print("정각이 아닙니다")

# fruit = ["사과","포도","홍시"]
# str = input()
# if str in fruit:
#     print("정답입니다")
# else:
#     print("땡")

# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# key = input("좋아하는 계절은: ")
# if val in fruit:
#     print("정답입니다!")
# else:
#     print("땡")

# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# value = input()
# if value in fruit.values():
#     print("정답입니다!")
# else:
#     print("땡!")

# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# just = input()
# if just in warn_investment_list:
#     print("투자 경고 종목입니다")
# else:
#     print("투자 경고 종목이 아닙니다")

# a = input()
# if a.islower():
#     print(a.upper())
# else:
#     print(a.lower())

# score = int(input())
# if score <= 100 and score >= 81:
#     print("A")
# elif score <= 80 and score >= 61:
#     print("B")
# elif score <= 60 and score >= 41:
#     print("C")
# elif score <= 40 and score >= 21:
#     print("D")
# else:
#     print("F")

# dic = {'달러': 1167, '엔': 1.096, '유로': 1216, '위안': 171}
# a = input()
# b , c = a.split()
# print(float(b)*dic[c])

# L = []
# for i in range(3):
#     a = int(input("input number: "))
#     L.append(a)
# L.sort(reverse=True)
# print(L[0])

# a = input()
# if a[0:3] == '011':
#     print("당신은 SKT 사용자입니다")
# elif a[0:3] == '016':
#     print("당신은 KT 사용자입니다")
# elif a[0:3] == '019':
#     print("당신은 LGU 사용자입니다")
# elif a[0:3] == '010':
#     print("ERROR 404 NO DATA FOUND")

# a = input()
# if a[2] == '0' or a[2] == '1' or a[2] == '2':
#     print("강북구")
# elif a[2] == '3' or a[2] == '4' or a[2] == '5':
#     print("도봉구")
# elif a[2] == '6' or a[2] == '7' or a[2] == '8' or a[2] == '9':
#     print("노원구")

# villagernumber, villagernumberend = input().split('-')
# if villagernumberend[0] == '1' or villagernumberend[0] == '3':
#     print("남자입니다")
# elif villagernumberend[0] == '2' or villagernumberend[0] == '4':
#     print("여자입니다")

villagernumber, villagernumberend = input().split('-')
if villagernumberend[1:3] == '8' or villagernumberend[2] == '7' or villagernumberend[2] == '6' or villagernumberend[2] == '5' or villagernumberend[2] == '4' or villagernumberend[2] == '3' or villagernumberend[2] == '2' or villagernumberend[2] == '1' or villagernumberend[2] == '0':
    print('서울주민입니다')
else:
    print('서울 주민 아니에요')