def tribonacci(signature, n):
    #your code here
    l = sum(signature)
    lst = [] + signature
    lst.append(l)
    for i in range(3, n):
        print(i)
        lst.append(lst[i]+lst[i-1]+lst[i-2])
    return lst[:n]

print(tribonacci([1,1,1], 10))