def compute_sum(n):
    su = 0
    for i in range(1,n+1):
        if len(str(i))>1:
            su+=sum(map(int, list(str(i))))
        else:
            su+=i
    return su

print(type(dir(2)))