class decrypter():
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
    
a = decrypter()

s = {
    1:a.nth2dec,
    2:a.dec2nth
}



