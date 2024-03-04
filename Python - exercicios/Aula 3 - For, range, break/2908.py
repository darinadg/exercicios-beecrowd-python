senha = input()
numDigitos = 0
numCaracteres = 0

for caractere in senha:
    if '0' <= caractere <= '9':
        numDigitos += 1

    numCaracteres += 1

if numDigitos >= 2 and numCaracteres >= 8:
    print('OK')
else:
    print('ERRO')