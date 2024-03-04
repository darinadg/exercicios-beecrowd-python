#1961 - Somando strings
#Seu programa deve ler três strings quaisquer e imprimir a soma dessas strings duas a duas, em todas as ordens possíveis.
#Deve fornecer Três linhas, cada uma com uma string qualquer
#Deve produzir Seis linhas, cada uma som a soma das string duas a duas. A ordem da impressão é a mesma ordem na qual as strings foram dadas, como nos exemplos. 


caractere1 = input()
caractere2 = input()
caractere3 = input()

print(caractere1 + caractere2)
print(caractere1 + caractere3)
print(caractere2 + caractere1)
print(caractere2 + caractere3)
print(caractere3 + caractere1)
print(caractere3 + caractere2)

