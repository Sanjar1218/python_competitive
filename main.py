dct = {'one': [1,2,3,4,5], 'two': [4,5,32,7,3]}


for x, y in dct.items():
    if x == 'one':
        dct[x].remove(3)
print(dct)