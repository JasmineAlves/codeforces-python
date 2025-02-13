'''
Resolução do problema: 'A. Team'
LINK: https://codeforces.com/problemset/problem/231/A

- a, b,c : Representa visão de Petya, Vânia e Tonya respectivamente
- split() : Divide string em partes, onde o espaço é o separador
- map (int, ...) : Converte cada elemento da lista para um número inteiro 
'''

# Lê número de problemas na competição
n = int(input())
write_solution = 0

# Loop para leitura da visão de cada participante em cada problema (n)
for _ in range(n):
    a, b, c = map(int, input().split())
    
    # Se pelo menos 2 participantes tiverem certeza, implementam o problema
    if (a + b + c >= 2):
        write_solution += 1

# Exibe o resultado
print(write_solution)