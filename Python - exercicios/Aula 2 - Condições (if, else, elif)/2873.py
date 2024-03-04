placa = int(input())

ultimo_digito = placa % 10

if 1 <= ultimo_digito <= 2:
    print("segunda-feira")
elif 3 <= ultimo_digito <= 4:
    print("terça-feira")
elif 5 <= ultimo_digito <= 6:
    print("quarta-feira")
elif 7 <= ultimo_digito <= 8:
    print("quinta-feira")
else:
    print("sexta-feira")
