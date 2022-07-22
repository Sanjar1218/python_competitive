def square(lst, n, m):
    l = []
    x, y = block(n, m)
    ind = {     
        0: range(0,3),
        1: range(3,6),
        2: range(6,9),
    }
    for a in ind[x]:
        for b in ind[y]: 
            l.append(lst[a][b]) 
    return f(l)

def block(n, m):
    x, y = 0, 0
    if m>=0 and m<3:
        y = 0
    elif m>=3 and m<6:
        y = 1
    elif m>=6 and m<9:
        y = 2
    if n>=0 and n<3:
        x = 0
    elif n>=3 and n<6:
        x = 1
    elif n>=6 and n<9:
        x = 2
    
    return x, y

def f(lst):
    l = [1,2,3,4,5,6,7,8,9]
    ls = []
    for i in l:
        if lst.count(i) ==0:
            ls.append(i)
    return ls