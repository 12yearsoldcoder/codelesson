# def solution(letter):
#     answer = ''
#     morse = {
#         '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
#         '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
#         '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
#         '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
#         '-.--': 'y', '--..': 'z'}
#     letter = letter.split()
#     for i in letter:
#         for k,v in morse.items():
#             if k == i:
#                 answer += v
#
#     return answer
# print(solution(".--. -.-- - .... --- -."))

# def solution(quiz):
#     answer = []
#     for i in quiz:
#         i = i.split()
#         a = int(i[0])
#         b = int(i[2])
#         if i[1] == "+":
#             c = a + b
#             if c == int(i[4]):
#                 answer.append("O")
#             else:
#                 answer.append("X")
#         elif i[1] == "-":
#             c = a - b
#             if c == int(i[4]):
#                 answer.append("O")
#             else:
#                 answer.append("X")
#     return answer
# print(solution(["3 - 4 = -3", "5 + 6 = 11"]))

# def solution(denum1, num1, denum2, num2):
#     rdnum = denum1 * num2 + denum2 * num1
#     rnum = num1 * num2
#     gcd = 0
#     for i in range(min(rdnum,rnum),1,-1):
#         if rdnum% i == 0 and rnum % i == 0:
#             gcd = i
#             break
#     if gcd != 0:
#     rdnum //= gcd
#     rnum //= gcd
#
#
#     return [rdnum,rnum]
def solution(dartResult):
    answer = 0
    score = []
    area = {"S":1,"D":2,"T":3}
    for result in dartResult:
        if len(score) == 0:
            score.append(result)
        elif result.isdigit():
            if type(score[-1]) == str:
                score.append(score.pop() + result)
            else:
                score.append(result)
        elif result in area:
            score.append(int(score.pop()) ** area[result])
        elif result == '*':
            if len(score) == 1:
                score.append(int(score.pop()) * 2)
            else:
                num2 = score.pop()
                num1 = score.pop()
                score.append(int(num1) * 2)
                score.append(int(num2) * 2)
        elif result == "#":
            score.append(int(score.pop()) * -1)
    answer = sum(score)
    return answer
print(solution("1S2D*3T"))