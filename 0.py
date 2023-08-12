def solution(people: list, limit: int):
    answer = 0
    for e,i in enumerate(people):
        clone = people[:]
        clone.pop(people.index(i))
        for j in clone:
            if i + j > 100:
                continue
            answer += 1
            people.remove(people.index(i))
            people.remove(people.index(j))

    return answer


print(solution([70, 50, 80, 50], 100))
