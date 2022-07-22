from math import factorial
def going(n):
    # your code
    print(n)
    u = factorial(n)
    sum = fact(n)
    s = str(((sum)/u)+1)
    return float(s[:8])
def fact(n):
    sum = 0
    x = 1
    for i in range(1,n):
        x *= i
        sum += x
    return sum

print(going(1011))