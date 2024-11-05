numero = int(input("Digite um numero"))
if numero > 0:
    print("O número é POSITIVO")
elif numero < 0:
    print("O número é NEGATIVO")
else:
    print("O número é 0")

idade = int(input("Digite sua idade"))

if idade >= 18:
    print("Você é maior de idade")
elif idade == 17:
    print("Você ainda é menor de idade, mas está quase lá!")
else:
    print("Você é menor de idade")
