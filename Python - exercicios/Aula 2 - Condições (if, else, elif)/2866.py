saldoBanco = int(input())
totalCompra = int(input())

if saldoBanco >= totalCompra:
    print('se você comprar tudo o saldo será:', saldoBanco - totalCompra)
else:
    print('seu saldo é insuficiente para essa compra')