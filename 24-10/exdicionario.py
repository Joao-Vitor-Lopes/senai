#EX01 - DICIONÁRIO

notas_aluno = {
    "João": "5",
    "Laura": "9",
    "Erick": "10"
}

print(notas_aluno["Laura"])

notas_aluno['Bruno'] = int(input("Qual a nota de Bruno? ")) 

print(notas_aluno)

novas_notas = {
    "João": "8",
    "Laura": "7",
    "Erick": "7",
    "Julia": "9"
}

notas_aluno.update (novas_notas)

print(notas_aluno)

#EX 02 - Acesso a Elementos

carro = {
    "marca": "Ford",
    "modelo": "Fiesta",
    "ano": "2020"
}

print(carro["marca"])
print(carro["modelo"])