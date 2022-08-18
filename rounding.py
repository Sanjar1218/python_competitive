from math import ceil, floor
def solution(n):
    l = len(str(n))
    x = 1
    for i in range(l-1):
        print(n)
        n = ceil(n/10)
        
        x *= 10

    return n*x

print(round(15/10))
print(solution(98765432))