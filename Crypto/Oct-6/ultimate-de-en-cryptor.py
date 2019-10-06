import random

num2rus = {}
rus_c = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'
for i in range(0, len(rus_c)):
    num2rus[i + 192] = rus_c[i]
rus2num = {v: k for k, v in num2rus.items()}

class decoder():
    def __init__(self):
        self.value = True

    def dec2nth(self, num, base):
        #Decimal in to number with Nth base
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
        #Number with Nth base to decimal
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
        #Binary to decimal
        return int(n, 2)

    def dec2bin(self, n):
        #Decimal to binary
        return bin(int(n))[2:]

    def dec2rus(self, n):
        #Decimal to russian character ( Win-1251 )
        if int(n) in num2rus.keys():
            return num2rus[int(n)]
        else:
            return chr(int(n))
    def chunks(self, l, n):
        #Split array of items by 4 in each
        for i in range(0, len(l), n):
            yield l[i:i + n]

    
    def elias_decode(self, s):
        #Decode Elias to deimals
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
            final.append(str(self.bin2dec(i)))

        return "".join(final)

    def binStr2bin(self, s, a, b):
        #Any series of two repeating characters to binary
        #Ex:  "ABABAB" -> 101010 if a=1, b=0
        return "".join(["1" if i == a else "0" for i in s])

    def reverseArray(self, n):
        return n[::-1]

class encoder(decoder):
    def __init__(self):
        self.valur = True

    def elias_encode(self, s):
        s = [rus2num[i] for i in s]

        return s

    def rus2num(self, s):
        #Russian characters ( Win1251 ) to num array
        return [rus2num[i] if i in rus2num else ord(i) for i in s]
    def caesar(self, text, s):
        #Caesar cipher | temporary only in ENG!!!
        result = ""
        for i in range(len(text)):
            char = text[i]
            if (char.isupper()):
                result += chr((ord(char) + s-65) % 26 + 65)
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
            return result
        text = "CEASER CIPHER DEMO"
        s = 4


a = decoder()
b = encoder()


s = "10110010 10100011 11010001 11101110 01000111 10101001 00110010 00101010 00100011 01001101 00100110 01001101 11110010 11".split(" ")
s = "".join(s)


#for i in list(a.chunks(a.elias_decode(s), 3)):
#    print(a.dec2rus(i))

print(a.elias_decode(s))
