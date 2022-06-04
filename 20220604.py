# 재귀, 기하

# 재귀
# 함수 안에서 함수 자기 자신을 호줄하는 방식

# def hello():
#     print('Hello, World!')
#     hello()
# hello()
# 재귀 깊이가 1000으로 정해져있어 에러
# -> 종료 조건 필요
# def hello(count):
#     if count == 0:
#         return
#     print('Hello, World!',count)
#     count -= 1
#     hello(count)
# hello(8)

# 백준 팩토리얼
# def faactorial(n):
#     anw = 1
#     if n > 0:
#         anw = n * faactorial(n - 1)
#     return anw
#
#
# print(faactorial(10))
# anw = 1
# n = int(input())
# if n > 0:
#     for i in range(1,n+1):
#         anw *= i
# print(anw)
# while True:
#     print(1)

# 백준 10870

n = int(input())
L = [0,1]

for i in range(1,n):
    a = L[0] + L[1]
    L.remove(L[0])
    L.append(a)
ans = L[1]
print(ans)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input())
print(fibonacci(n))
