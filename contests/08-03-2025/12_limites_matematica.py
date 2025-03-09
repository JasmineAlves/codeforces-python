b = int(input())

if (b == 1 or b == 0):
    print(1)
else:
    for a in range(0, b):
        if a**a == b:
            print(a)
            exit()
        elif (a**a > b): 
            break
        
    print(-1)