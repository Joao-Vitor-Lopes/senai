#Exercício 3: Tabuada

numero = int(input("Digite um número para fazer a tabuada dele: "))

contador = 0

print(f"Tabuada do número: {numero}")

while contador <= 10:
    
    multiplicacao = numero * contador
    print(f"{numero} x {contador} = {multiplicacao}")
    contador = contador + 1

#Exercício 4: Soma de Números Positivos

numero2 = float(input("Digite um número positivo para ser somado (ao digitar um número negativo irá para de somar e mostrar o resultado final)\n"))

numero3 = 0

while numero2 >= 0 and numero3 >= 0:
    
    numero2 = numero2 + numero3
    
    numero3 = float(input(f"o resultado é {numero2}\nContinue digitando um número para ser somado: "))
    
print(f"A soma dos números é {numero2}")

#Exercício 5: Contagem de Números Pares

contador = 1
contador_pares = 0
while contador != 0:
    contador = int(input("Contador de números pares (Aperte a tecla 0 para sair) ou o número par para ser contado: "))
    if contador % 2 == 0:
         contador_pares = contador_pares + 1
    else:
        
            print("Erro! O número digitado é impar")
            
           
    
contador_pares = contador_pares - 1
print(f"Você digitou {contador_pares} números pares")
            


