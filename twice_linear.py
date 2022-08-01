def dbl_linear(n):
    lst = [1]
    m=0
    for i in lst:
        m+=1
        y = 2*i+1
        x = 3*i+1
        lst.append(x)
        lst.append(y)
        lst = list(sorted(set(lst)))
        print(i)
        if n == m:
            print(lst)
            return list(set(lst))[n]
        # dct[f'y{i}'] = y
        # dct[f'x{i}'] = x
    return -1
print(dbl_linear(20))