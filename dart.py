def dart(dartResult):
    answer = 0
    score = []
    for result in dartResult:
        if result.isdigit():
            lst = list(dartResult)
            ind = lst.index(result)
            if lst[ind + 1] == 'S':
                score.append(int(result))
            elif lst[ind + 1] == 'D':
                score.append(int(result) ** 2)
            elif lst[ind + 1] == 'T':
                score.append(int(result) ** 3)
        else:
            if result == '*':
                for sc in score:
                    del score[score.index(sc)]
