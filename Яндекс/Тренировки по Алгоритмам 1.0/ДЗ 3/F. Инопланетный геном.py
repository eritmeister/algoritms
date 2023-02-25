st = set()
a = input()
b = input()
for i in range(1, len(b)):
    st.add(b[i-1:i+1])
cnt = 0
for i in range(1, len(a)):
    if a[i-1:i+1] in st:
        cnt += 1
print(cnt)
