limit = int(input())
pairs = {}

def div_sum(number):
    return sum(x for x in range(1, (number // 2)+1) if number % x == 0)
    
for i in range(1, limit + 1):
    aggr = div_sum(i)
    if i == div_sum(aggr) and i != aggr :
        pairs[i] = aggr

for i in pairs.keys():
    if i != limit and pairs[i] != limit:
        print(i, pairs[i])