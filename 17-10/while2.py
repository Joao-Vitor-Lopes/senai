# ctrl + k + c (comentar)
# ctrl + k + u (descomentar)

import os
import platform

def limpar_sistema():
    sistema = platform.system()
    
    if sistema == "Windows":
        os.system('cls')
        
    else:
        os.system('clear')

def obrigado():
    print("Obrigado por utilizar o sistema")
    
    

while True:
    
    limpar_sistema()
    obrigado()
    
    print("Hello world!")
    nome = input("Digite seu nome")
    print(f"Seja bem vindo {nome}")
    
    resposta = input("Deseja continuar s/n: ").strip() .lower()
    
    if resposta != "s":
        break
    