lst = list(map(int, input().split()))
for i in range(1, len(lst)):
    if lst[i] <= lst[i-1]:
        print('NO')
        break
else:
    print('YES')
