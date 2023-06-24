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
    if not A or A == '0':
        return "A가 잘못 정의되었습니다."

    A = int(A)
    B = int(B)
    C = int(C)

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
                        if int(d) == 1 and int(f) == 1:
                            return f"(x {op1} {abs(e)}) (x {op2} {abs(int(g))})"
                        elif int(d) == 1:
                            return f"(x {op1} {abs(e)}) ({int(f)}x {op2} {abs(int(g))})"
                        elif int(f) == 1:
                            return f"({int(d)}x {op1} {abs(e)}) (x {op2} {abs(int(g))})"
                        return f"({int(d)}x {op1} {abs(e)}) ({int(f)}x {op2} {abs(int(g))})"
        x1 = (-B + (B ** 2 - 4*A*C) ** 0.5)/(2*A)
        op1 = '+' if x1 > 0 else '-'
        x2 = (-B - (B ** 2 - 4*A*C) ** 0.5)/(2*A)
        op2 = '+' if x2 > 0 else '-'

        return f"(x {op1} {abs(x1): .4lf}) (x {op2} {abs(x2): .4lf})"
    elif B ** 2 - 4*A*C == 0:
        d = m.sqrt(A)
        e = m.sqrt(C)

        if e == 0:
            return f"{d}x"
        op = '+' if B > 0 else '-'
        if int(d) == 1:
            return f"(x {op} {int(e)})²"
        return f"({int(d)}x {op} {int(e)})²"
    elif B ** 2 - 4*A*C < 0:
        return "해가 없습니다."
