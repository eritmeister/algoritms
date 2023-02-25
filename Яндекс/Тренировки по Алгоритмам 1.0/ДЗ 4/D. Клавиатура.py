n = int(input())
keys = list(map(int, input().split()))
cnt = [0] * (n + 1)
k = int(input())
for p in list(map(int, input().split())):
    cnt[p] += 1
for i in range(n):
    if cnt[i + 1] > keys[i]:
        print('YES')
    else:
        print('NO')
