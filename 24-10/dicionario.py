agenda = {
    "Ana": "11992659874",
    "João": "15985473658",
    "Camila": "11985698745"
}

print(agenda["Camila"])

lanchonete = {"Salgado": 4.50, "Lanche": 6.50, "Suco": 3.00, "Refrigerante": 3.50}

for produto, preco in lanchonete.items():
    print(produto, preco)