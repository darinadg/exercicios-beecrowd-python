condicaoParada = input()
contador = 0
while True:
    linha = input()
    if linha == condicaoParada:
        break
    contador += 1
print(contador)