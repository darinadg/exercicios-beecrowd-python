irma1 = input()
irma2 = input()
irma3 = input()
irma4 = input()

if irma1 >= irma2 and irma1 >= irma3 and irma1 >= irma4:
  maior = irma1
elif irma2 >= irma1 and irma2 >= irma3 and irma2 >= irma4:
  maior = irma2
elif irma3 >= irma1 and irma3 >= irma2 and irma3 >= irma4:
   maior = irma3
else:
  maior = irma4

print('A mais velha tem', maior, 'anos')
