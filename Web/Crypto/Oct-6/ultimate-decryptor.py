import random

win1251 = {}

rus = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯфбвгдежзийклмнопрстуфхцчшщъыьэюя'
for i in range(0, len(rus)):
    win1251[i + 192] = rus[i]

class decoder():
    def __init__(self):
        self.value = True

    def dec2nth(self, num, base):
        if num == 0:
            return "0"
        else:
            num = int(num)
            digs = []
            while num:
                digs.append(str(int(num % base)))
                num //= base
            return "".join(digs[::-1])

    def nth2dec(self, num, base):
        if base <= 10:
            figures = [int(i) for i in str(num)] 
        else:
            figures = [int(i,base) for i in str(num)]
        figures = figures[::-1]
        result = 0
        for i in range(len(figures)):
            result += figures[i] * base ** i
        return result

    def bin2dec(self, n):
        return int(n, 2)

    def dec2bin(self, n):
        return bin(int(n))[2:]

    def dec2rus(self, n):
        if n in win1251.keys():
            return win1251[n]
        else:
            return chr(int(n))
    def chunks(self, l, n):
        for i in range(0, len(l), n):
            yield l[i:i + n]

    
    def elias_decode(self, s):
        prefix = int(s[0])
        s = [int(i) for i in s[1:]]
        fragments = []
        start = 0
        c = 0
        i = 0
        while i < len(s):
            if c:
                if s[i] == 0:
                    c += 1
                elif s[i] == 1:
                    fragments.append("".join(str(j) for j in s[start:i + c + 1]))
                    i += c
                    c = 0
            else:
                if s[i] == 1:
                    fragments.append("1")
                elif s[i] == 0:
                    start = i
                    c += 1
            i += 1

        result = [self.bin2dec(i) for i in fragments]

        l = []

        for i in result:
            for i in range(0, i):
                l.append("1" if prefix else "0")
            prefix = 0 if prefix else 1

        final = []

        for i in list(self.chunks("".join(l), 8)):
            final.append(self.dec2rus(self.bin2dec(i)))

        return "".join(final)

    def binStr2bin(self, s, a, b):
        return "".join(["1" if i == a else "0" for i in s])




a = decoder()



