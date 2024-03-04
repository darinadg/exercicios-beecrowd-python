placarTime1 = 0
placarTime2 = 0

while True:
    ponto = int(input())
    if ponto == 1:
        placarTime1 += 1
    elif ponto == 2:
        placarTime2 += 1
    
    if placarTime1 >= 25 or placarTime2 >= 25:
        diferencaPontos = placarTime1 - placarTime2
        if not (placarTime1 == placarTime2 and placarTime1 >= 24 and diferencaPontos == 0):
            if diferencaPontos >= 2 or diferencaPontos <= -2:
                break

print(placarTime1, "x", placarTime2)