def diversor():
    x = int(input('podaj liczbe a to  cudo sprawdzi czy ma diversor'))
    y = []
    for i in range(1, x+1):
        if x % int(i) == 0:
            y.append(i)
    if len(y) == 2:
        print('liczba pierwsza')
    print(y)


diversor()
