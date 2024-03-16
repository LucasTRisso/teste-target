palavra = str(input("Digite uma palavra: "))
inverso = str()

for i in range(len(palavra) - 1, -1, -1):
    inverso = inverso + palavra[i]

print(inverso)
