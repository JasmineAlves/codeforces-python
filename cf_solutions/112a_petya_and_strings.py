'''
Resolução do problema: 'A. Petya and Strings'
LINK: https://codeforces.com/problemset/problem/112/A

- str.casefold() : Destinado a comparações sem distinções de caixa
    > Outra opção seria a aplicação de 'srt.lower()'
'''

# Recebe entradas e aplica o método 'str.casefold()'
s1 = input().casefold()
s2 = input().casefold()

# Realiza as comparações de forma lexografica - próprio do Python - e exibe resposta
if (s1 == s2):
    print(0)
elif (s1 > s2):
    print(1)
else:
    print(-1)    