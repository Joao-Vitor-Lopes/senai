'''numeros = [1,2,3,4,5]
soma = 0

for contador in numeros:
    soma += contador
print(f"A soma dos números é {soma}")'''

for numero in range(1,11):
    if numero == 5:
        print("Número 5 encontrado, saindo")
        break
    elif numero %2 == 0:
        continue
print(f"Número impar {numero}")