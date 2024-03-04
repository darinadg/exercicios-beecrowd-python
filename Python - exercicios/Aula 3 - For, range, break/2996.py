eleitores = int(input())
votosFavor = 0
votosContra = 0
votosOutros = 0

for item in range(eleitores):
    voto = input()
    
    if voto == 'F':
        votosFavor += 1
    elif voto == 'C':
        votosContra += 1
    else:
        votosOutros += 1

print('a favor:', votosFavor)
print('contra:', votosContra)
print('outros:', votosOutros)