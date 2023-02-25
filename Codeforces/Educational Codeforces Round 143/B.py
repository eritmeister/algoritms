for _ in range(int(input())):
    pairs = []
    f1, f2 = False, False
    n, k = list(map(int, input().split()))
    for i in range(n):
        l, r = list(map(int, input().split()))
        if l == k:
            f1 = True
        if r == k:
            f2 = True
    if f1 and f2:
        print('YES')
    else:
        print('NO')
