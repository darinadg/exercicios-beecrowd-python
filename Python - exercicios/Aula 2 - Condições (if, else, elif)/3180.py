palavra1 = input()
palavra2 = input()
palavra3 = input()

if palavra1 in palavra2 and not palavra1 in palavra3:
    print(palavra1, "CONTIDO EM", palavra2, "MAS", palavra1, "NÃO CONTIDO EM", palavra3)
elif palavra1 in palavra3 and not palavra1 in palavra2:
    print(palavra1, "NÃO CONTIDO EM", palavra2, "MAS", palavra1, "CONTIDO EM", palavra3)
elif palavra1 in palavra2 and palavra1 in palavra3:
    print(palavra1, "CONTIDO EM", palavra2, "E", palavra1, "CONTIDO EM", palavra3)
else:
    print(palavra1, "NÃO CONTIDO EM", palavra2, "E", palavra1, "NÃO CONTIDO EM", palavra3)

