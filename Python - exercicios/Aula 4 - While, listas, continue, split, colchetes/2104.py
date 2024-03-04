palavra = input()
letrasDigitadas = ''

while True:
    letra = input()
    if letra == '.':
        break
    letrasDigitadas += letra

if letrasDigitadas == palavra:
    print(True)
else:
    print(False)