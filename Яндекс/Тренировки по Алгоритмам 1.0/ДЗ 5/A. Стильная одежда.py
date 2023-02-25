N = int(input())
ncolors = list(map(int, input().split()))
M = int(input())
mcolors = list(map(int, input().split()))
delta, n, m = abs(ncolors[0] - mcolors[0]), ncolors[0], mcolors[0]
f, s = 0, 0
while f < N and s < M:
    if ncolors[f] < mcolors[s]:
        if mcolors[s] - ncolors[f] < delta:
            delta = mcolors[s] - ncolors[f]
            n = ncolors[f]
            m = mcolors[s]
        f += 1
    elif mcolors[s] < ncolors[f]:
        if ncolors[f] - mcolors[s] < delta:
            delta = ncolors[f] - mcolors[s]
            n = ncolors[f]
            m = mcolors[s]
        s += 1
    else:
        n = ncolors[f]
        m = mcolors[s]
        break
print(n, m)
