for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    s1 = input()
    s2 = input()
    k = 0
    for i in range(1, n):
        if s1[i] == s1[i-1]:
            k += 1
    for i in range(1, m):
        if s2[i] == s2[i-1]:
            k += 1
    if k == 0:
        print('YES')
    elif k == 1:
        if s1[-1] == s2[-1]:
            print('NO')
        else:
            print('YES')
    else:
        print('NO')
