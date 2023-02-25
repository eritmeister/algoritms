n = int(input())
d = dict()
for _ in range(n):
    ln, h = list(map(int, input().split()))
    if ln not in d:
        d[ln] = h
    elif h > d[ln]:
        d[ln] = h
res = 0
for key in d.keys():
    res += d[key]
print(res)
