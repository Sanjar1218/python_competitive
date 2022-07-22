def next_smaller(n):
    lst = list(str(n))
    rlst = lst[::-1]
    klst = lst[::-1]
    l = len(lst)
    if sorted(lst) == lst or len(str(n))==1:
        return -1
    for i in range(l-1):
        if rlst[i] < rlst[i+1]:
            x = rlst[i]
            print('bosh',rlst)
            print('p', x)
            print(rlst[i+1])
            rlst[i] = rlst[i+1]
            rlst[i+1] = x 
            print('oxiri', rlst)
            break
    p = ''.join(rlst)
    print(p)
    b= False
    for i in range(l-1):
        if b:
            break
        for n in range(i, l-1):
            if klst[i] < klst[n]:
                x = klst[i]
                print('k', x)
                klst[i] = klst[n]
                klst[n] = x
                b= True
    k = ''.join(klst[::-1])
    return p if p>k else k

print(next_smaller(917))