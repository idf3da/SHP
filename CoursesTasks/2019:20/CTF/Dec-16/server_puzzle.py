import random, string

# initialise identity map
map = []                             # empty list
for i in range(256):
    map.append(chr(i))
# permute map
i = 255
while i > 0:
    j = int(random.randint * (i+1))        # 0 <= j <= i
    map[i], map[j] = map[j], map[i]  # swap entries
    i = i - 1
# create string translation table
