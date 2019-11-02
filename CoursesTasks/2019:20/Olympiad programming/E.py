input()
n = list(map(int, input().split()))

print(list(sorted(set(n)))[-2])