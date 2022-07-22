def next_higher(value):
    x= format(value, "b")
    y = format(129, "b")
    print(y)
    print('kata',int('11000000',2))
    x = int(x, 2)+ int(y, 2)
    print(int(y,2))
    return x 

print(next_higher(127))