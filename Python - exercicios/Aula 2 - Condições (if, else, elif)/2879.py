simboloOperações = input()
valor1 = int(input())
valor2 = int(input())

if simboloOperações == '+':
    resultado = valor1 + valor2
elif simboloOperações == '-':
    resultado = valor1 - valor2
elif simboloOperações == '*':
    resultado = valor1 * valor2
elif simboloOperações == '/':
    resultado = valor1 / valor2
elif simboloOperações == '//':
    resultado = valor1 // valor2
elif simboloOperações == '%':
    resultado = valor1 % valor2
elif simboloOperações == '**':
    resultado = valor1 ** valor2

print(resultado)