numCandidatas = int(input())
emailsInvalidos = 0

for i in range(numCandidatas):
    email = input()
    if '@' not in email or '.' not in email:
        emailsInvalidos += 1
print(emailsInvalidos)