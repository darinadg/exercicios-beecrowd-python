cpf = input()
cpfSemPontos = ''
num = '0123456789'
    
for caracteres in cpf:
  if caracteres not in '.-':
        cpfSemPontos += caracteres
            
if len(cpfSemPontos) == 11:
  if caracteres in num:
        print(cpfSemPontos)
if caracteres not in num:
        print('ENCODING ERROR')
if len(cpfSemPontos) != 11:
        print('SIZE ERROR')
       