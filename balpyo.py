def solution(polynomial):
    answer = ''
    polynomial = polynomial.split(' + ')
    a = polynomial.count('x')
    for i in range(1,101):
        if f'{i}'+'x' in polynomial:
            b = f'{i+a}'+'x'
            polynomial[polynomial.index(f'{i}'+'x')] = b
            for j in polynomial:
                if j == 'x':
                    del polynomial[polynomial.index(j)]
            for j in polynomial:
                answer += j + ' ' + '+' + ' '
            answer = answer.strip()
            answer = answer.strip('+')
            answer = answer.strip()
            break
        return answer


print(solution("3x + 7 + x"))