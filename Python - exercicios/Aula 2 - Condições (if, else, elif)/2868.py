idade = int(input())

if idade < 16:
    print('Jovem demais para votar, espere até 16')
elif idade >= 18 and idade <= 69:
    print('Seu voto é obrigatório')
else:
    print('Seu voto é facultativo: você pode votar ou não')
