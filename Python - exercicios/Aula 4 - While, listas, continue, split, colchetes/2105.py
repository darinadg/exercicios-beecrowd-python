palavraCorreta = input()

while True:
    tentativa = ''
    while True:
        letra = input()
        if letra == '.':
            break
        tentativa += letra
    if tentativa == palavraCorreta:
        print("8-)")
        break
    else:
        print("8-|")