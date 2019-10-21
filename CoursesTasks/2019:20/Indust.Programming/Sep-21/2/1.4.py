
def has_nums(a):
    flag = False
    for i in a:
        if i.isnumeric():
            flag = True
    return flag

def has_uppers(a):
    flag = False
    for i in a:
        if i.isupper():
            flag = True
    return flag

def has_lowercases(a):
    flag = False
    for i in a:
        if i.islower():
            flag = True
    return flag

l = input()
print("YES" if len(l) > 7 and has_nums(l) and has_lowercases(l) and has_uppers(l) else "NO")



