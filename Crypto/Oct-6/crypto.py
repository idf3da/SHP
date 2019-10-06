import random

rus_ascii1 = {}
rus_chars = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'

for i in range(0, len(rus_chars)): rus_ascii1[i + 192] = rus_chars[i]
rus_ascii2 = {v: k for k, v in rus_ascii1.items()}

rus_ascii = {**rus_ascii1, **rus_ascii2}
# If there's any other way to convert ascii
# number to Win1251 please make an issue
# on GitHub.

# Note that all function return <str>

def dec2nth(num, base):
    #Decimal int to number with Nth base
    if num:
        num = int(num)
        base = int(base)
        digs = []
        while num:
            digs.append(str(int(num % base)))
            num //= base
        return "".join(digs[::-1])
    else:
        return "0"

def nth2dec(num, base):
    base = int(base)
    figs = [int(i) if base <= 10 else int(i, base) for i in str(num)]

    figs = figs[::-1]
    res = 0
    for i in range(len(figs)):
        res += figs[i] * base ** i
    return str(res)

def bin2dec(n):
    #Binary to decimal
    return str(int(str(n), 2))

def dec2bin(n):
    #Decimal to binary
    return bin(int(n))[2:]

def dec2rus(n):
    #Decimal to russian character ( Win-1251 )
    if int(n) in rus_ascii.keys():
        return rus_ascii[int(n)]
    else:
        return chr(int(n))

def rus2dec(s):
    #Russian characters ( Win1251 ) to num array
    return [str(rus_ascii[i]) if i in rus_ascii else str(ord(i)) for i in s]

def chunk(l, n):
    #Split array of items by n in each
    for i in range(0, len(l), int(n)): yield l[i:i + int(n)]

def elias2dec(s):
    #Decode Elias to deimals
    prefix = int(s[0])
    s = [int(i) for i in s[1:]]
    frags = []
    start = 0
    c = 0
    i = 0
    while i < len(s):
        if c:
            if s[i] == 0:
                c += 1
            elif s[i] == 1:
                frags.append("".join(str(j) for j in s[start:i + c + 1]))
                i += c
                c = 0
        else:
            if s[i] == 1:
                frags.append("1")
            elif s[i] == 0:
                start = i
                c += 1
        i += 1
    result = [bin2dec(i) for i in frags]
    l = []
    for i in result:
        for j in range(0, int(i)):
            l.append("1" if prefix else "0")
        prefix = 0 if prefix else 1
    final = []
    for i in list(chunk("".join(l), 8)):
        final.append(str(bin2dec(i)))

    return final
    # Exception: line 14

def str2bin(s, a, b):
    #Any series of two repeating characters to binary
    #Ex:  "ABABAB" -> 101010 if a=1, b=0
    return "".join(["1" if i == a else "0" for i in s])

def reverseArray(n):
    return n[::-1]

def convert2(s, t):
    return str(s) if t == "str" else int(s) if t == "int" else list(s)


############
## To Doo ##
############

# Sibirsky triangle/pyrhamid