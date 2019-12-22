x = [5, 10, 15]
y = []


def listend(x, y):
    z = len(x)-1
    y.append(x[0])
    y.append(x[z])
    return y


print(listend(x, y))
