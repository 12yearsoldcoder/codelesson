def solution(lines):
    answer = 0
    cnt = []
    for i in lines: # i = 리스트
        for j in range(min(i),max(i)):
            if j not in cnt:
                cnt.append(j)
            else:
                del cnt[cnt.index(j)]
                answer += 1
    return answer
