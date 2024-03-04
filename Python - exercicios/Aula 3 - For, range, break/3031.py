
cpf = input()
cpfSemPontos = ""

for caracteres in cpf:
    if '0' <= caracteres <= '9':
        cpfSemPontos += caracteres

if len(cpfSemPontos) == 11:
    print(cpfSemPontos)
    print('OK')
else:
    print(cpfSemPontos)
    print('ERROR')