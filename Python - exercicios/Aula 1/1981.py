nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())
nota5 = float(input())
peso1 = float(input())
peso2 = float(input())
peso3 = float(input())
peso4 = float(input())
peso5 = float(input())

somatoriaPesos = (peso1 + peso2 + peso3 + peso4 + peso5)
pontosTotais = ((nota1 * peso1) + (nota2 * peso2) + (nota3 *peso3) + (nota4 * peso4) + (nota5 * peso5)) / somatoriaPesos

print('%.1f' % pontosTotais)

