from math import log
def power_of_two(x):
    if x==0:
        return False
    n = log(2,x)%1
    print(n)
    return n==0

print(power_of_two(536870912))