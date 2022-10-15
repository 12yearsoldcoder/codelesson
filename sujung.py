def solution(polynomial):
    answer = ''
    polynomial = polynomial.split('+')
    for i in polynomial:
        polynomial[polynomial.index(i)] = i.strip()
    a = polynomial.count('x')
    while 1:
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
            break
    else: #오류 원인: i가 1일때 조건을 총족하지 못하고 else실행 후 break
        answer = f'{a}'+'x'
        break
    return answer

print(solution("3x + 7 + x"))