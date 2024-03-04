# Leitura do valor mínimo
valor_minimo = int(input())

# Leitura dos valores
valores = []
while True:
    entrada = input()
    if entrada == "":
        break
    valores += [int(entrada)]

# Cálculo do total
total = 0
for i in range(len(valores)):
    total += valores[i]

# Cálculo da sobra
sobra = total - valor_minimo
if sobra < 0:
    sobra = 0

# Impressão dos resultados
print("minimo", valor_minimo)
print("total", total)
print("sobra", sobra)
