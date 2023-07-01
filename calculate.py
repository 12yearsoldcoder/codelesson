import math as m


def divisor(a):
    b = range(1, a)
    c = []
    for i in b:
        if a % i == 0:
            c.append(i)
    c.append(a)
    return c


def solution(A, B, C):

    try:
        A = int(A)
        B = int(B)
        C = int(C)
    except:
        return "입력이 잘못되었습니다. 정수를 입력해주세요."

    if not A or A == '0':
        return "A가 잘못 정의되었습니다."


    if B ** 2 - 4*A*C > 0:
        divisor_A = divisor(A)
        divisor_C = divisor(C)

        divisor_A += list(map(lambda x: -x, divisor_A))
        divisor_C += list(map(lambda x: -x, divisor_C))
        for d in divisor_A:
            for e in divisor_C:
                f = A/d
                g = C/e
                if d*g + e*f == B:
                    if d > 0 or e > 0:
                        op1 = '+' if e > 0 else '-'
                        op2 = '+' if g > 0 else '-'
                        d = str(d).replace('0.', '')
                        if d in ['-1', '1']:
                            d = d.replace('1', '')
                        f = str(f).replace('0.', '')
                        if f in ['-1', '1']:
                            f = f.replace('1', '')
                        return f"({int(d)}x {op1} {abs(e)}) ({int(f)}x {op2} {abs(int(g))})"
        x1 = (-B + (B ** 2 - 4*A*C) ** 0.5)/(2*A)
        op1 = '+' if x1 > 0 else '-'
        x2 = (-B - (B ** 2 - 4*A*C) ** 0.5)/(2*A)
        op2 = '+' if x2 > 0 else '-'
        print(f"{op1}\n{abs(x1): .4lf}\n{op2}\n{abs(x2)}")
        return f"(x {op1} {abs(x1): .4lf}) (x {op2} {abs(x2): .4lf})"
    elif B ** 2 - 4*A*C == 0:
        d = m.sqrt(A)
        e = m.sqrt(C)
        d = str(d)
        if d in ['-1', '1']:
            d = d.replace('1', '')
        if e == 0:
            return f"{d}x"
        op = '+' if B > 0 else '-'
        if int(d[0:d.index('.')]) == 1:
            return f"(x {op} {int(e)})²"
        return f"({int(d)}x {op} {int(e)})²"
    elif B ** 2 - 4*A*C < 0:
        return "해가 없습니다."