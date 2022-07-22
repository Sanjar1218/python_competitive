def alphabet_position(text):
    text = text.lower().replace(' ', '')
    lst = []
    for i in text:
        if ord(i)>96 and ord(i)<123:
            lst.append(str(ord(i)-96))
    return ' '.join(lst)

print(alphabet_position("The sunset sets at twelve o' clock.")+'|')