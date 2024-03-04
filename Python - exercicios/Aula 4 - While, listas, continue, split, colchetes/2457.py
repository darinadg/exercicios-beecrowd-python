memoriaMaxima = 0
memoriaAtual = 0

while True:
    requisicao = int(input())
    if requisicao == 0:
        break
    memoriaAtual += requisicao
    memoriaMaxima = max(memoriaMaxima, memoriaAtual)
    if memoriaAtual < 0:
        memoriaAtual = 0

print(memoriaMaxima)