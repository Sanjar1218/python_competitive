def persistence(n):
    while len(str(n))!=1:
        print(n)
        lst = map(int, list(str(n)))
        n =1
        for i in lst:
            print('i', i)
            n*=i
            print('n', n)
    return n

print(persistence(39))