s = 0
e = (' гений ')
while 1 > s:
    h = input('ввод имени')
    d = lambda a,b: a+b
    print(d(h, e))
    if h == 'off':
        break