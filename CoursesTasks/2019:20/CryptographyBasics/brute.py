import itertools
print(*[''.join(x) for x in itertools.product('!!_', repeat=3)], sep='\n')