input()
lst = list(map(int, input().split()))
x = int(input())
nearest = lst[0]
for i in range(1, len(lst)):
    if abs(x - lst[i]) < abs(x - nearest):
        nearest = lst[i]
print(nearest)
