
irma1 = int(input())
irma2 = int(input())
irma3 = int(input())
irma4 = int(input())

if irma1 >= irma2 and irma1 >= irma3 and irma1 >= irma4:
  maior = irma1
elif irma2 >= irma1 and irma2 >= irma3 and irma2 >= irma4:
  maior = irma2
elif irma3 >= irma1 and irma3 >= irma2 and irma3 >= irma4:
   maior = irma3
else:
  maior = irma4

if irma1 <= irma2 and irma1 <= irma3 and irma1 <= irma4:
  menor = irma1
elif irma2 <= irma1 and irma2 <= irma3 and irma2 <= irma4:
  menor = irma2
elif irma3 <= irma1 and irma3 <= irma2 and irma3 <= irma4:
   menor = irma3
else:
  menor = irma4

print('A mais velha tem', maior)
print('A mais nova tem', menor)