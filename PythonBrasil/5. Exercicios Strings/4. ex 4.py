""" 4. Nome na vertical em escada. Modifique o programa anterior de forma a mostrar
o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO

"""

nome = str.upper(input('Digite um nome: '))

for x in range(0, len(nome) + 1):
    print(nome[:x])
