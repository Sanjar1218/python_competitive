def row(lst, n):
    for u in range(n):
        l = []
        for i in range(n):
            l.append(lst[u][i])
        if len(l) != len(set(l)):
            return False
    return True

def column(lst, n):
    for u in range(n):
        l = []
        for i in range(n):
            l.append(lst[i][u])
        if len(l) != len(set(l)):
            return False
    return True


def square(lst, n):
    step = round(n**0.5)
    for x in range(0, n,step):
        for y in range(0, n, step):
            l = []
            for i in range(x, x+step):
                for u in range(y, y+step):
                    l.append(lst[i][u])
            print(l)
            if len(l) != len(set(l)):
                return False
    return True

puzzle =[[8, 5, 7, 1, 3, 9, 6, 4, 2], [6, 1, 3, 2, 8, 4, 7, 9, 5], [2, 9, 4, 6, 5, 7, 1, 3, 8], [7, 2, 6, 5, 9, 8, 3, 1, 4], [5, 3, 8, 4, 7, 1, 2, 6, 9], [1, 4, 9, 3, 6, 2, 8, 5, 7], [3, 6, 2, 0, 4, 5, 9, 7, 1], [9, 8, 5, 7, 1, 3, 4, 2, 6], [4, 7, 1, 9, 2, 6, 5, 8, 3]]
puzzle2 = [
    [3, 4, 5, 6, 2, 1, 9, 7, 8], 
    [6, 7, 9, 5, 8, 3, 2, 1, 4], 
    [2, 1, 8, 7, 4, 9, 6, 3, 5], 
    [8, 2, 3, 1, 7, 6, 5, 4, 9], 
    [5, 6, 1, 3, 9, 4, 8, 2, 7], 
    [7, 9, 4, 8, 5, 2, 3, 6, 1], 
    [1, 5, 7, 2, 6, 8, 4, 9, 3], 
    [4, 3, 2, 9, 1, 5, 7, 8, 6], 
    [9, 8, 6, 4, 3, 7, 1, 5, 2]]

print(square(puzzle, 9))
print(row(puzzle, 9))
print(column(puzzle, 9))