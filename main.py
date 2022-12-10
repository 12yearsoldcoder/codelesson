# import math
# def solution(s):
#     a = ""
#     answer = 0
#     for i in s:
#         if i == "1":
#             a += "1"
#     for ind,num in enumerate(a):
#         answer += int(num)*int(math.pow(int(num),ind))
#     return answer
# solution("00011011")
# import math
# def solution(n):
#     current = n
#     strin = ""
#     answer = 0
#     while current != 0:
#         strin += str(current % 3)
#         current = current // 3
#     a = 0
#     for i in range(len(strin)-1, -1, -1):
#         answer += int(strin[a]) * pow(3,i)
#     print(answer)
# solution(45)

def solution(n: int, arr1: list, arr2: list):
    for i in range(len(arr1)):
        a = bin(arr1[i])
        b = bin(arr2[i])
        a = a[2:]
        b = b[2:]
        if len(a) < 6:
            for j in range(6-len(a)-1):




solution(5,[9,20,28,18,11],[30,1,21,17,28])