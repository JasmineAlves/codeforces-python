'''
Resolução do problema 'A. Bit++'
LINK: https://codeforces.com/problemset/problem/282/A

- n : Recebe o número de instruções do programa
- x : Variável fundamental do Bit++
'''

n = int(input())
x = 0

# Loop para atender o número de instruções que serão inseridas
for _ in range(n):
    operation = input()
    
    # Se a operação corresponde a um incremento em 'x'
    if (operation == 'X++' or operation == '++X'):
        x += 1
    # Se a operação corresponde a um decremento em 'x'
    elif (operation == 'X--' or operation == '--X'):
        x -= 1

# Exibe o resultado        
print(x)