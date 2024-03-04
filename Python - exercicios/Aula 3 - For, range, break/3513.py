massa_carro = float(input())
num_voltas = int(input())

melhor_volta, maior_aceleracao = 0, 0.0

for volta in range(1, num_voltas + 1):
    aceleracao = float(input())
    aceleracao_media = aceleracao / massa_carro

    if aceleracao_media > maior_aceleracao:
        maior_aceleracao, melhor_volta = aceleracao_media, volta

maior_aceleracao = "%.1f" % maior_aceleracao

print('melhor_volta:', melhor_volta)
print('maior aceleração:', maior_aceleracao)