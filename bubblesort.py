def Bubble_sort(_list: list, reverseopt= False):
    if reverseopt ==False:
        for i in range(len(_list) - 1):
            for j in range(len(_list) - 1 - i):
                if _list[j] > _list[j+1]:
                    tmp = _list[j]
                    _list[j] = _list[j + 1]
                    _list[j+1] = tmp
        print(_list)
    elif reverseopt == True:
        for i in range(len(_list) - 1):
            for j in range(len(_list) - 1 - i):
                if _list[j] < _list[j+1]:
                    tmp = _list[j]
                    _list[j] = _list[j + 1]
                    _list[j+1] = tmp
        print(_list)
Bubble_sort([1,5,4,2,3,6,8,7,9,0], True)