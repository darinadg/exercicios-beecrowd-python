valorDisponivel = float(input())

itensComprados = 0

while True:
    valorItem = float(input())

    if valorItem <= valorDisponivel:
        valorDisponivel -= valorItem
        itensComprados += 1
    else:
        break  

print("Número de itens", itensComprados)
print("Saldo: %.2f" % valorDisponivel)