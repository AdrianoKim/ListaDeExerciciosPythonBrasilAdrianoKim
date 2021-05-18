""" 8.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês."""

hr = float(input('Digite o valor ganho por cada hora trabalhada: '))
qtde = float(input('Digite a quantidade de horas trabalhadas no mês: '))
amount = hr * qtde
currency = '{:,.2f}'. format(amount)

print('O salário bruto total referente ao mês trabalhado é: ', 'R$', currency)
