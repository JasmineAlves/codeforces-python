'''
Resolução do problema: 'A. Next Round'
LINK: https://codeforces.com/problemset/problem/158/A

- n : Quantidade de participantes
- k : Posição de corte
- split() : Divide string (padrão do input) em partes, onde o espaço é o separador
- map (int, ...) : Converte cada elemento da lista para um número inteiro 
'''

# Lê número de participantes, posição de corte
n, k = map(int, input().split())

# Lê pontuações - outra opção seria usando list(...)
scores = input().split()  
for i in range(n):  
    scores[i] = int(scores[i])  

# Confere pontução mínima
limit_scr = scores[k-1]

# Contagem de número de participantes que irão avançar para a próxima partida
advance = 0
for score in scores:
    if score >= limit_scr and score > 0:
        advance += 1

# Exibe o resultado
print(advance)

