observacoes = []

while True:
    entrada = float(input())
    if entrada < 0:
        pior_estimativa = entrada
        break
    observacoes += [entrada]  # Adiciona cada entrada à lista de observações

# Contagem das observações inferiores à pior estimativa
total_observacoes = 0
inferiores = 0

for valor in observacoes:
    total_observacoes += 1
    if valor < pior_estimativa:
        inferiores += 1

# Decrementamos 1 do total de observações, pois não queremos contar o valor negativo como uma observação válida
total_observacoes -= 1 if total_observacoes > 0 else 0

# Saída
print(total_observacoes, inferiores)