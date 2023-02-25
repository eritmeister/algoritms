input()
lst = list(map(int, input().split()))
for i in range(len(lst)):
    if lst[i] != lst[-i-1]:
        print