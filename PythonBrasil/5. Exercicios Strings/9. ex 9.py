""" 9. Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de
CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação
dos dígitos verificadores edos caracteres de formatação.

"""


def verificarnumeros(cpf):
    for posicao, caractere in enumerate(cpf):
        if posicao != 3 and posicao != 7 and posicao != 11 and not caractere.isdigit():
            return True
    return False


cpf = input('Digite o CPF no formato (xxx.xxx.xxx-xx): ')

while verificarnumeros(cpf) or cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
    cpf = input('CPF invalido!\nDigite o CPF no formato (xxx.xxx.xxx-xx) :')

print('O CPF foi cadastrado com sucesso.')
