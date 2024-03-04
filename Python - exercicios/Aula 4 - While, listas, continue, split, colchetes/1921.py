linha1 = input()
linha2 = input()
linha3 = input()
linha4 = input()

valorBinario = linha1 + linha2 + linha3 + linha4

valorDecimal = 0
tamanho = len(valorBinario)

for i in range(tamanho):
    valorDecimal += int(valorBinario[i]) * 2 ** (tamanho - 1 - i)

print(valorDecimal)