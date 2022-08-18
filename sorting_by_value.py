dct = {"Java": 10, "Ruby": 80, "Python": 65}

def sort_by_value(dct):
    return dict(sorted(dct.items(), key=lambda x: x[1], reverse=True))

print(sort_by_value(dct))