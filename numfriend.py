def solution(X, Y):
    answer = ''
    l = []
    Y = list(Y)
    cnt_x = []
    cnt_y = []
    for i in range(10):
        cnt_x.append(X.count(str(i)))
        cnt_y.append(Y.count(str(i)))
    for i in range(10):
        if cnt_x[i] > 0 and cnt_y[i] > 0:
            l.append(str(i) * min(cnt_x[i], cnt_y[i]))
    l.sort(reverse=True)
    l = list(l)
    for i  in range(10,1):
        if '0' * i
    if len(l) == 0:
        return '-1'
    else:
        for i in l:
            answer += i
        return answer
print(solution("100", "203045"))