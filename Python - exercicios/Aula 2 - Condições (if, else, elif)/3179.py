caractere = input()

if '0' <= caractere <= '9':
    print('algarismo')

elif caractere in 'aeiouAEIOU':
    print('vogal')

elif caractere in '@#$%&*()_-+=!':
    print('especial')

else:
    print('outro')
