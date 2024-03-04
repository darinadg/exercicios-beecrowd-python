piorEstimativa = float(input())
numValores = int(input())

contadorSuperior = 0

for item in range(numValores):
    taxa = float(input())

    if taxa > piorEstimativa:
        contadorSuperior += 1

print(contadorSuperior)