""" 18. Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado
de download do arquivo usando este link (em minutos).
"""
import math

tam = float(input('Digite o tamanho do arquivo (em MB): '))
vel = float(input('Digite a velocidade do link (em Mbps.): '))
# Conversao de MegaBIT para MegaBYTE por segundo:
mb = vel * 0.125

print('O tempo aproximado de download será: ', math.ceil((tam/mb)/60), 'minuto(s).')
