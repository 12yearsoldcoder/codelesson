# def solution(brown: int, yellow: int):
#     total = brown + yellow
#     for tx in range(3,total // 3 + 1):
#         ty = total // tx
#         if tx * ty == total and (tx - 2) * (ty - 2) == yellow: return [max(tx,ty),min(tx,ty)]
    # a = 2
    # l = [1]
    # while a <= yellow:
    #     if yellow % a == 0:
    #         l.append(a)
    #     a += 1
    # if len(l) <= 2:
    #     wid = yellow + 2
    #     hei = (brown + yellow) / wid
    # else:
    #     b = len(l)
    #     c = l[:b // 2 + 1]
    #     wid = max(c) + 2
    #     d = c.index(max(c)) - 1
    #     hei = d + 2
    # return [wid, hei]



