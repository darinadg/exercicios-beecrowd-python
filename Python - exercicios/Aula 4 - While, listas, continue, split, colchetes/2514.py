numeroVagas = int(input())
inscritos = []
contador = 0

while True:
    inscrito = input()
    if inscrito == '.':
        break
    contador += 1
    inscritos += [inscrito]

vagasFaltando = numeroVagas - contador

if vagasFaltando > 0:
    print("vagas sobrando: %.f" % vagasFaltando)
elif vagasFaltando <0:
    print("vagas faltando: %.f" % -vagasFaltando)