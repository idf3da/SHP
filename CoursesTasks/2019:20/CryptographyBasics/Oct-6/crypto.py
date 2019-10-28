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
    return bin(int(n))[2:].zfill(8)

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
    #for i in list(chunk("".join(l), 8)):
    #    final.append(str(bin2dec(i)))

    #return final
    return "".join(l)
    # Exception: line 14

def str2bin(s, a, b):
    #Any series of two repeating characters to binary
    #Ex:  "ABABAB" -> 101010 if a=1, b=0
    return "".join(["1" if i == a else "0" for i in s])

def reverseArray(n):
    return n[::-1]

def convert2(s, t):
    return str(s) if t == "str" else int(s) if t == "int" else list(s)

def sibisky_UL2UR2any(s):
    s = list(s)
    print("So.. Obviously first two letters are")
    print("<",*s[:2], "> ", "Index 1 and 2.", sep='')
    L = input("Third letter in message: ")
    if s.count(L) == 0:
        pass
    else:
        ix = [i for i,val in enumerate(s) if val == L]
        print("There are multiple", L)
        print("Which one?")
        print(*s)
        for i in range(len(s)):
            if i in ix:
                print("^", end=' ')
            else:
                print(" ", end=' ')
        print()
        print(ix)
        print()
    pos = int(input("Index: "))
    bp = []
    print("All Korrect. This is encd blueprint.")
    print("If blueprints sum(asterics) == len(message): pass")
    for i in range(pos - 1, 0, -1):
        bp.append(i)
        print("* " * i)
    diff = len(s) - sum(bp)
    print(bp)
    print("Your diffrence is", diff, "it will be")
    print("appended descendingly.")
    i = 0
    while diff:
        bp[i] += 1
        i += 1
        diff -= 1
    for i in bp:
        print("* " * i)
    c = 0
    for i in bp:
        print(s[c:c+i])
        c += i

    #So flippin' hard
    #I will
    pass
    
        






def Hemming15_112bin(s):
    bs = [0, 0, 0, 0]
    s = list(s)
    for i in range(0, len(s)):
        bp = str(bin(i + 1)[2:]).zfill(4)
        if bp[-1] == "1":
            bs[-1] += int(s[i])
        if bp[-2] == "1":
            bs[-2] += int(s[i])
        if bp[-3] == "1":
            bs[-3] += int(s[i])
        if bp[-4] == "1":
            bs[-4] += int(s[i])
    bs = ["0" if i % 2 == 0 else "1" for i in bs]
    ep = int("".join(bs), 2)
    if ep:
        s[ep - 1] = "0" if s[ep - 1] == "1" else "1"
    del s[0]
    del s[0]
    del s[1]
    del s[4]
    return "".join(s)

def dropEl(s, n):
    del s[n]
    return s

def binMorse2dec(n):
    mc = {
        "00000" : "0",
        "10000" : "1",
        "11000" : "2",
        "11100" : "3",
        "11110" : "4",
        "11111" : "5",
        "01111" : "6",
        "00111" : "7",
        "00011" : "8",
        "00001" : "9"
    }
    return mc[n]

def OddEven2bin(n):
    return "0" if int(n) % 2 == 0 else "1"

def RLE(s, n):
    # s is a list
    start = n
    result = []
    for i in s:
        result.append(int(i) * str(start))
        start = "0" if start == "1" else "1"
    return result

def tabReplacementPassword(s, password):
    res = []
    for i in range(0, len(s) // len(password)):
        res.append(list(s[i::4]))
    print(list(password))
    print(*res, sep='\n')
    password = [int(rus2dec(i)[0]) - 223 for i in list(password)]
    
    for i in range(0, len(password)):
        index = password.index(min(password))
        print(index + 1)
        del password[index]


############
## To Doo ##
############

# Sibirsky triangle/pyrhamid    
# Hemming recovery             ++++++++
# Drop element                 ++++++++
# Mul replacement 000 111 222 -> 012 012 012
# tab replacement

#sibisky_UL2UR2any("Всуюниролдщаиивеедедамащотзёкьиен!ду?жон")
#sibisky_UL2UR2any("Чтопсьотоо-млеян")

tabReplacementPassword("ыеиттх  мжтс  мьоое ", "банан")