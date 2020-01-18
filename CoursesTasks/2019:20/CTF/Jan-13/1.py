s = '''1234567890-=_+─┬␊⎼├≤┤␋⎺⎻[]▒⎽␍°±␤┘┐┌;'\<≥│␌┴␉┼└,./QWERTYUIOPπ£ASDFGHJKL:"≠ZXCVBNM<>?'''
k = '''1234567890-=_+qwertyuiop[]asdfghjkl;'\<zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?'''
t = '''⎽␤⎻␌├°π┬␊┌␌⎺└␊ ├⎺ ├␤␊ ┤┼␋│£'''

d = {}

for i in range(0, len(s)):
    d[s[i]] = k[i]



for i in t:
    try:
        print(d[i], end='')
    except:
        pass