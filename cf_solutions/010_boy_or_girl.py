'''
Resolução do problema 'A. Boy or Girl'
LINK: https://codeforces.com/problemset/problem/236/A

- set(name) : Armazena apenas elementos únicos, removendo repetições
- len(new_name) : Verifica tamanho da string
'''

# Recebe o nome do usuário
name = input()
# Remove repetições
new_name = set(name)

# Verifica se o número de caracteres distintos é par e retorna resposta
if (len(new_name) % 2 == 0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")