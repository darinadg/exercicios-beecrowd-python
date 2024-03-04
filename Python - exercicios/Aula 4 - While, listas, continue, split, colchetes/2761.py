linha1 = input()
linha2 = input()

for item in linha2:
    linha1 = linha1.replace(item, '*')

print(linha1)