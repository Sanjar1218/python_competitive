import re

def abbreviate(s):
    
    car = re.findall(r'[^a-zA-Z]+', s)
    print(car)
    word = re.split(r'[^a-zA-Z]+', s)
    if len(word) == 1:
        return s[0] + str(len(s)-2)+s[-1]
    lst = []
    print(s)
    for i in word:
        print(i)
        if len(i) ==0:
            continue
        if len(i) == 1:
            lst.append(i)
            continue
        lst.append(i[0] + (str(len(i)-2) if len(i)>3 else i) + i[-1])
    st = lst[0]
    for x in range(1,len(lst)):
        st+=car[x-1]+lst[x]
    return st+car[-1] if len(word)==len(car) else st

# print(abbreviate("the balloon. cat-monolithic'is, mat. double-barreled; double-barreled5"))
word = 'asd123faewfa,asdf233ae.cz923424'
print(re.findall(r'$@[0-9a-zA-Z]{8}(?<=.[A-Za-z0-9]+)', word))