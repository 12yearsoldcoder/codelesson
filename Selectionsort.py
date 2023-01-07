list = [3,1,5,7,2,4,6]
def Selection_sort(list: list, reverse= False):
    for i in range(len(list) - 1):
        minimum = i
        for j in range(1 + i, len(list)):
            if list[minimum] > list[j]:
                minimum = j
        tmp = list[i]
        list[i] = list[minimum]
        list[minimum] = tmp
        print(list)


Selection_sort(list)