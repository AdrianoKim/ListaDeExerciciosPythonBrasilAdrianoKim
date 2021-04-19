""" 7. Conta espaços e vogais.
Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco),
conte:

a. quantos espaços em branco existem na frase.
b. quantas vezes aparecem as vogais a, e, i, o, u.

"""


frase = input('Digite uma frase: ')
espaco = 0
a = 0
e = 0
i = 0
o = 0
u = 0

for esp in frase:
    if esp in ' ':
        espaco += 1
print('Quantidade de espacos em branco na frase: ', espaco)

for vog in frase:
    if vog in 'a':
        a += 1
    elif vog in 'e':
        e += 1
    elif vog in 'i':
        i += 1
    elif vog in 'o':
        o += 1
    elif vog in 'u':
        u += 1
print('Quantidade de vogais: \nA: %d\nE: %d\nI: %d\nO: %d\nU: %d' % (a, e, i, o, u))
