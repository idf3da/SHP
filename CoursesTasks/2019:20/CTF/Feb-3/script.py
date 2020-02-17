import requests
import binascii
import os

url = "http://188.225.34.174:8337/"

s = ""
a = "armmpujuspqwcqcqwcqwecttttttt"

res = requests.get(url+s)

while res.status_code != 202:
    for i in a:
        res = requests.get(url+s+i)
        print("     ", s, i, sep='')
        if res.status_code == 200:
            s += i
        if res.status_code == 202:
            os.exit(1)
    print(url+s)

print(url, s)
