def solution(dots):
    x = [dots[0][0], dots[1][0]]
    y = [dots[0][1], dots[1][1]]
    x.sort(reverse=True)
    y.sort(reverse=True)
    print(x)
    print(y)
    if x[0] == x[1]:
        a = x[0]
    else:
        a = x[0] - x[1]
    if y[0] == y[1]:
        b = y[0]
    else:
        b = y[0] - y[1]
    return a * b


dotss = [[-1, -1], [1, 1], [1, -1], [-1, 1]]
solution(dotss)
