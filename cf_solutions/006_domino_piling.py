'''
Resolução do problema: 'A. Domino Piling'
LINK: https://codeforces.com/problemset/problem/50/A

- m, n : Representa a quantidade de quadrados do eixo 'x' e 'y' do tabuleiro
- split() : Divide string em partes, onde o espaço é o separador
- map (int, ...) : Converte cada elemento da lista para um número inteiro 
'''

# Atribui os valores corretamente a 'm' e 'n'
m, n = map(int, input().split())

# Calcula quantas peças de dominó podem ser colocados no tabuleiro - uma peça ocupa 2 quadrados
domino = int((m*n)/2)

# Exibe o resultado
print(domino)
