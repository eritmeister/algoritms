st = set()
n = int(input())
for i in range(n):
    a, b = list(map(int, input().split()))
    if a + b + 1 == n and a >= 0 and b >= 0:
        st.add((a, b))
print(len(st))
