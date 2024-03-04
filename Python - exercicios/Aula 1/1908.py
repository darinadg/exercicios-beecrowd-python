numeroMinutos = int(input())

numeroHoras = numeroMinutos // 60
minutosRestantes = numeroMinutos % 60

print(numeroMinutos,'min =',numeroHoras,'h',minutosRestantes,'min', sep='')
