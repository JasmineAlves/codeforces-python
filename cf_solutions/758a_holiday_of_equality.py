'''
Resolução do problema 'A. Holiday Of Equality'
LINK: https://codeforces.com/problemset/problem/758/A

- split() : Divide string (padrão do input) em partes, onde o espaço é o separador
- map (int, ...) : Converte cada elemento da lista para um número inteiro 
- list() : Converte em lista
- max() : Retorna o valor mais alto do grupo
'''

# Recebe o número de cidadãos
citizens = int(input())
# Recebe o número de bem-estar de cada cidadão (em burles)
welfare = list(map(int, input().split()))

# Inicializa para uso posterior
new_wf = []
min_burles = 0

# Descarta qualquer número extra adicionado, por meio de uma nova lista
for i in range(citizens):
    new_wf.append(welfare[i])

# Verifica qual o maior número da nova lista
highest = max(new_wf)

# Verifica a diferença de cada indivíduo e incrementa ao total (burles)
for i in range(citizens):
    if new_wf[i] < highest:
        min_burles += (highest - new_wf[i])

# Exibe o resultado
print(min_burles)


