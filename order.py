import re
def unique_in_order(iterable):
    return [(i[0] if len(i)>0 else i) for i in re.findall('\w+', iterable)]

# print(unique_in_order('AAAABBBCCDAABBB'))
print(re.findall('^\w{3}$', 'AAAABBBCCDAABBB'))