def dictonary(puzzle):
    dct = {}
    for i in range(9):
        for x in range(9):
            if puzzle[i][x] == 0:
                pos = []
                sq = square(puzzle,i,x) 
                for t in sq:
                    if row(puzzle, i, t) and column(puzzle, x, t):
                        pos.append(t)
                dct[f'{i},{x}'] = pos 
    return dct
def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    dct = dictonary(puzzle) 
    while True:
        print(dct)
        b = True
        for k, v in dct.items():
            print(k, v)
            x, y = map(int, k.split(',')) 
            if len(v) == 1:
                b = False
                de = v[0]
                puzzle[x][y] = de
                dct[k] = []
                rem(dct, x, y, de)
        if b:
            break
    dct = dictonary(puzzle)
    while True:
        print(dct)
        b = True
        for k, v in dct.items():
            print(k, v)
            x, y = map(int, k.split(',')) 
            if len(v) == 1:
                b = False
                print(k, v)
                de = v[0]
                puzzle[x][y] = de
                dct[k] = []
                rem(dct, x, y, de)
            elif len(v) == 2:
                print('elif')
                b = False
                ls = kor_square(x, y)
                ls.remove(k)
                print('ls', ls)
                for i in ls:
                    u, o = map(int, i.split(','))
                    if i in dct.keys():
                        if dct[i] == v:
                            rem(dct, u, o, v[0], k)
                            rem(dct, u, o, v[1], k)
        if b:
            break
    return puzzle

def rem(dct, x, y, target, ig='9,9'):
    for k, v in dct.items():
        if k != ig and (str(x) == k[0] or str(y) == k[-1]):
            if target in v:
                dct[k].remove(target)
 
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

def kor_square(x, y):
    x, y = block(x,y)
    lst = []
    ind = {     
        0: range(0,3),
        1: range(3,6),
        2: range(6,9),
    }
    for a in ind[x]:
        for b in ind[y]:
            lst.append(f'{a},{b}')
    return lst   

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

def f(lst):
    l = [1,2,3,4,5,6,7,8,9]
    ls = []
    for i in l:
        if lst.count(i) ==0:
            ls.append(i)
    return ls

def row(lst, n, target):
    l = []
    for i in range(9):
        l.append(lst[n][i])
    if l.count(target) != 0:
        return False 
    return True 

def column(lst, n, target):
    l = []
    for i in range(9):
        l.append(lst[i][n])
    if l.count(target) != 0:
        return False
    return True 

puzzle = [[0, 4, 6, 0, 0, 0, 0, 0, 0], 
          [9, 0, 2, 0, 6, 0, 0, 0, 8], 
          [0, 0, 8, 4, 0, 0, 2, 5, 0], 
          [0, 0, 0, 8, 0, 0, 0, 7, 0], 
          [5, 0, 0, 7, 0, 2, 0, 0, 3], 
          [0, 1, 0, 0, 0, 6, 0, 0, 0], 
          [0, 6, 4, 0, 0, 3, 9, 0, 0], 
          [3, 0, 0, 0, 8, 0, 1, 0, 2], 
          [0, 0, 0, 0, 0, 0, 7, 3, 0],]

puzzle2 = [[0, 0, 6, 0, 2, 0, 0, 5, 0], [0, 0, 2, 0, 0, 0, 1, 9, 4], [0, 0, 0, 1, 0, 0, 2, 0, 7], [6, 0, 7, 0, 8, 2, 0, 1, 9], [0, 8, 5, 0, 7, 0, 0, 3, 0], [0, 0, 0, 6, 0, 5, 4, 0, 0], [0, 9, 0, 0, 1, 3, 0, 4, 0], [0, 0, 1, 0, 0, 9, 0, 0, 0], [7, 3, 0, 0, 0, 8, 9, 0, 0]]



p = [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
    [6, 7, 2, 1, 9, 5, 3, 4, 8], 
    [1, 9, 8, 3, 4, 2, 5, 6, 7], 
    [8, 5, 9, 7, 6, 1, 4, 2, 3], 
    [4, 2, 6, 8, 5, 3, 7, 9, 1], 
    [7, 1, 3, 9, 2, 4, 8, 5, 6], 
    [9, 6, 1, 5, 3, 7, 2, 8, 4], 
    [2, 8, 7, 4, 1, 9, 6, 3, 5], 
    [3, 4, 5, 2, 8, 6, 1, 7, 9]]
if __name__ == '__main__':
    # print('column', column(puzzle, 2))
    # print(square(puzzle, 1, 0))
    print(sudoku(puzzle2))
