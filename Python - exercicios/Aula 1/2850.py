totalConta = float(input())
porcentagemCliente = int(input())

valorGorjeta = totalConta * (porcentagemCliente / 100)
valorTotal = totalConta + valorGorjeta

print('%.2f' % valorTotal)

