def count_subsequences(a, b):
    x = 0
    count = 0
    for i in b:
        if i == a[x]:
            count +=1
        x+=1
        if x== len(a):
            x=0
    print(count)
    

print(count_subsequences("happy birthday", "appyh appy birth day"))