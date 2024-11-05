#Exercício 1: Impressão de Números em uma Lista

numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)


#Exercício 2: Tabuada

numero = int(input("Digite um número para ver sua tabuada: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

    
#Exercício 3: Soma de Elementos de uma Lista

lista3 = [2,4,6,8,10]
soma = 0

for contador in lista3:
    soma = soma + contador
print(f"A soma de todos os números é {soma}")

#Exercício 4: Contagem de Letras em uma String

string = input("Digite uma string: ")
contador_letras = 0

for letra in string:
    if letra.isalpha():  
        contador_letras += 1

print(f"Total de letras na string: {contador_letras}")


