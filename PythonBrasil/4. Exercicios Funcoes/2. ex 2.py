""" 2. Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário.
Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""


def imprimelinha(numero):
    for n in range(1, numero + 1):
        print('{}   '.format(n), end='')
    print()


def imprimesequencia(numero):
    for numero in range(numero + 1):
        imprimelinha(numero)


n1 = input('Digite um número: ')

imprimesequencia(int(n1))
