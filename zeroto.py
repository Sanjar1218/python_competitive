def going(n):  
    s = 1.0
    for i in range(2, n + 1):
        s = s/i + 1
        print(s)
    print(s)
    return int(s * 1e6) / 1e6
    
print(going(5))
print(33/120)