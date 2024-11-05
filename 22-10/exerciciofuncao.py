#EX 01 - Função para verificar maior número

def maior_numero(a,b):
    if a > b:
        return a
    if b > a:
        return b

a = int(input("Digite um número: "))
b = int(input("Digite um segundo número: "))
resultado = maior_numero(a,b)

print(f"O número {resultado} é maior")

#EX 02 - Função para somar dois números

def soma(n1,n2):
    return n1 + n2

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

resultado1 = soma(n1,n2)

print(f"A soma dos números é {resultado1}")

#EX 03 - Função para verificar se um número é par

def eh_par(numeros):
    
    if numeros % 2 == 0:
        return True
    else:
        return False
        
numeros = int(input("Digite um número"))



print(eh_par(numeros))


#EX 04 - Função para calcular a média de notas

def calcular_media(nota1, nota2, nota3):
    resultado2 = (nota1+nota2+nota3)/3
    if resultado2 >= 7:
        return "Você está aprovado"
    if resultado2 < 7 and resultado2 >= 5:
        return "Você está de recuperação"
    if resultado2 < 5:
        return "Você está reprovado"


nota1 = int(input("Digite sua nota de matemática: "))
nota2 = int(input("Digite sua nota de português: "))
nota3 = int(input("Digite sua nota de história: "))

print(calcular_media(nota1,nota2,nota3))