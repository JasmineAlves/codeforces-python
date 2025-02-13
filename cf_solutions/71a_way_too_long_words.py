
'''
Resolução do problema: 'A. Way Too Long Words'
LINK: https://codeforces.com/problemset/problem/71/A
'''

n = int(input())

for i in range(n):
    word = input()
    if len(word) > 10:
        a10n = word[0] + str(len(word) - 2) + word[-1]
        print(a10n)
    else:
        print(word)
    