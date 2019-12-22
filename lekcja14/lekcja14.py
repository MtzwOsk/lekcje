x = [1, 1, 2, 3, 4, 5, 7, 5]


def remover(list1):
    list2 = []
    for i in (list1):
        if i not in list2:
            list2.append(i)
    return list2


print(remover(x))


def setremover(list1):
    y = list(set(list1))
    return y


print(setremover(x))
