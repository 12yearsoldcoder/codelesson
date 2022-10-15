def solution(X, Y):
    answer = ''
    l = []
    whagin = []
    Y = list(Y)
    dic = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    x_cnt = [X.count('1'),X.count('2'),X.count('3'),X.count('4'),X.count('5'),
             X.count('6'),X.count('7'),X.count('8'),X.count('9')]
    y_cnt = [Y.count('1'),Y.count('2'),Y.count('3'),Y.count('4'),Y.count('5'),
             Y.count('6'),Y.count('7'),Y.count('8'),Y.count('9')]
    if len(l) == 0:
        l.append("-1")
    l.sort(reverse=True)
    for i in l:
        answer += i
    # 시간초과의 만병통치약은 딕셔너리?

    return answer


print(solution("12321", "42531"))
