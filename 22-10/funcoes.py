'''

def fazer_bolo(sabor):
    print(f"O bolo será de: {sabor}")
    print("Misturando os ingredientes")
    print("Assando o bolo")
    print("Bolo pronto!")

fazer_bolo("Chocolate")

def multiplicar_numeros(a,b):
    return a * b

resultado = multiplicar_numeros(7,6)
print(f"A multiplicação de 7 * 6 é: {resultado}")
'''

def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in frase:
        if letra in vogais:
            contador += 1
    return contador

frase = "Programar em python é DEMAIS!"
resultado = contar_vogais(frase)
print(f"A frase tem {resultado} vogais")
