seq = str(input())
key = "hello"
i = 0

for c in seq:
    if (c == key[i]):
        i += 1
    if i == len(key):
        break

if i == len(key):
    print("YES")
else:
    print("NO")