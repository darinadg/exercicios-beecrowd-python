numero = int(input())
pin = ''

erro = False
for item in range(numero):
    algarismo = input()

    if algarismo in pin:
        erro = True
        

    pin += algarismo

if erro:
    print('ERRO')
else:
    print('OK')

    
    