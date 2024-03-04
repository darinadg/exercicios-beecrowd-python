numero = int(input())
inicio = int(input())
fim = int(input())
print('Tabuada do', numero, 'de', inicio, 'até', fim)

if 1 <= numero <= 99 and 1 <= inicio <= 999 and 1 <= fim <= 999:
    for i in range(inicio, fim + 1):
        resultado = numero * i
        print(numero, "x", i, "=", resultado)
