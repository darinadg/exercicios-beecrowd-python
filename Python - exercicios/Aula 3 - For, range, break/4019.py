num_listas = int(input())
total_exercicios_resolvidos = 0

for lista in range(num_listas):
    num_exercicios = int(input())
    
    for exercicio in range(num_exercicios):
        total_exercicios_resolvidos += 1

print(total_exercicios_resolvidos)