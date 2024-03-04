valor = int(input())

if valor <= 0:
  print('Digite um valor inteiro positivo')
else:
  for item in range(1, valor + 1):
    print(item)