linhas = []
while True:
    linha = input()
    if linha == 'CDA':
        break
    linhas += [linha]

linhas += ['CDA 1942']

for linha in linhas:
    print(linha)