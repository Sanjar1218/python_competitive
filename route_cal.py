import re
def calculate(n):
    exp = "[\+\-$\*]"
    num = "\d"
    e = re.split(exp, n)
    numbers = re.split(num, n)
    print(e)
    print(numbers)



s = "5+8-8.8*2$4"
calculate(s)