#EX 01 - TUPLAS CORES

cores = ("Azul", "Vermelho", "Amarelo", "Roxo")
print(f"A primeira cor é {cores[0]}")
print(f"A última cor é {cores[3]}")
print(f"Aqui está todas as cores registradas {cores}")

#EX 02 - Criação de Tupla

frutas = ("maçã", "banana", "laranja", "uva")
print(frutas)

#EX 03 - Acesso a Elementos

dados = (10,20,30,40,50)
print(f"O segundo elemento é {dados[1]}")
print(f"O quarto elemento é {dados[3]}")

#EX 04 - Contagem de Elementos

numeros = (1,2,3,4,2,2)

contador = 0
for numero in numeros:
    if numero == 2:
        contador += 1

resultado = contador
print(f"A lista de números possue {resultado} numeros 2")
