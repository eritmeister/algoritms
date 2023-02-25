from collections import deque


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    d = deque()
    for i in range(n):
        cnt = 0
        d.append(a[i])
        for j in range(len(d)-1, -1, -1):
            delta = min(b[i], d[j])
            d[j] -= delta
            cnt += delta
        while len(d) > 0:
            if d[0] == 0:
                d.popleft()
            else:
                break
        c.append(cnt)
    print(*c)
