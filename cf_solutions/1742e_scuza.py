from bisect import bisect_right

t = int(input())

for i in range(t):
    n, q = map(int, input().split())
    
    a = list(map(int, input().split()))
    k = list(map(int, input().split()))

    soma_deg = [0] * (n + 1)
    altmax = [0] * (n + 1)

    for j in range(1, n + 1):
        soma_deg[j] = soma_deg[j - 1] + a[j - 1]
        altmax[j] = max(altmax[j - 1], a[j - 1]) 

    final = []
    
    for ki in k:
        ultimo = bisect_right(altmax, ki) - 1
        final.append(soma_deg[ultimo])

    print(" ".join(map(str, final)))
