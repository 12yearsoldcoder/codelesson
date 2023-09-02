# def main():
#     l = []
#     n = int(input())
#     data = 0
#     link = 0
#     cnt = 0
#     for i in range(n):
#         l.append(int(input()))
#     for i in l:
#         if i == 0:
#             cnt -= data
#             data = link
#             print(link)
#         else:
#             cnt += i
#             link = data
#             print(link)
#             data = i
#     print(cnt)
#
# if __name__ == '__main__':
#     main()

# K = int(input())
# arr = []
# for _ in range(K):
#     x = int(input())
#     if x:
#         arr.append(x)
#     else:
#         arr.pop()
# print(sum(arr))

# n = int(input())
# l = []
# case_cnt = 1
# for i in range(n):
#     l.append(input())
# for i in l:
#     string = ""
#     slices = i.split()
#     back = slices[-1]
#     slices[-1] = slices[0]
#     slices[0] = back
#     for j in slices:
#         string += j + ' '
#     print(f"Case #{case_cnt}: {string.rstrip()}")
#     case_cnt += 1
# a, l= input().split(), []
# for i in a: l.append(int(i))
# print(sum(l))
#
# import sys
# n = int(input())
# l = []
# stack = []
# for i in range(n):
#     inp = sys.stdin.readline()
#     l.append(inp.strip('\n'))
# for i in l:
#     if i[0] == '1':
#         stack.append(i[2])
#     if i[0] == '2':
#         try:
#             print(stack[1:])
#         except:
#             print(-1)
#     if i[0] == '3':
#         print(len(stack))
#     if i[0] == '4':
#         if len(stack) == 0:
#             print(1)
#         else:
#             print(0)
#     if i[0] == '5':
#         try:
#             print(stack[0])
#         except:
#             print(-1)

inp = input()
dic = {'H' : 1, 'C' : 12, 'O' : 16}
start_end = False
not_Parenthesis = 0
Parenthesis = 0
for i in inp:
    if i == '(':
        start_end = True
        continue
    elif i == ')':
        start_end = False
        continue
    if i.isalnum():
        if start_end
    if not start_end:
        not_Parenthesis += dic[i]
print(Parenthesis + not_Parenthesis)
