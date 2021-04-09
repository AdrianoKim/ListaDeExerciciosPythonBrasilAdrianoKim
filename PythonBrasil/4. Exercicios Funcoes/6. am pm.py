""" 6. Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
A entrada é dada em dois inteiros.
Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída.
Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M.
Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
Inclua um loop que permita que o usuário repita esse cálculo para
novos valores de entrada todas as vezes que desejar.
"""


def converter_hora(hora):
    if hora > 12 and hora != 24:
        contador = 0
        for x in range(hora):
            if x >= 12:
                contador += 1
        return contador
    elif hora == 24:
        return 0
    else:
        return hora


controle = 1

while controle != 0:
    hora = int(input("Digite a hora a ser convertida: "))
    minuto = input("Digite o minuto: ")
    if hora > 12 and hora != 24:
        inf = 'PM'
    else:
        inf = 'AM'
    print('Hora convertida :', converter_hora(hora), ':', minuto, inf)
    controle = int(input("Deseja realizar outra conversao? 1(sim)/0(nao): "))

if controle == 0:
    print('Programa encerrado.')
    exit()
