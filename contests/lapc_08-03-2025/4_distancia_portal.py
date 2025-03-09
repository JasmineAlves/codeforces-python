m = []

for i in range(5):
    ln = list(map(int, input().split()))
    m.append(ln)

for i in range(5):
    for j in range(5):
        if(m[i][j] == 1):
            x = i + 1
            y = j + 1
            break
        
min = abs(x - 3) + abs(y - 3)

print(min)