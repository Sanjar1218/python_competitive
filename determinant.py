def determinant(matrix):
    sum = 0
    min = 0
    for i in range(len(matrix)):
        k = 1
        b = 1
        print('for')
        for x in range(len(matrix)):
            k *= matrix[x][(x+i)%len(matrix)]
            print('matrix', x,(x+i)%len(matrix))
            print(k)
            b *= matrix[x][-(x+i+1)%len(matrix)]
            print('matrix2', x,-(x+i+1)%len(matrix))
            print(b)
        sum+=k
        min+=b
    return sum-min
m1 = [
[4, 6],
[3, 8]]
m5 = [
[2,4,2],
[3,1,1],
[1,2,0]]
print(determinant(m5))