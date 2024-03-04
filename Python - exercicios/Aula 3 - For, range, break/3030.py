cpf = input()

cpfSemPontosTraços = ""
for caractere in cpf:
    if '0' <= caractere <= '9':
        cpfSemPontosTraços += caractere

print(cpfSemPontosTraços)