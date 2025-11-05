from prompt_toolkit.shortcuts import choice
from enum import Enum
from datetime import datetime

lista = []
concluidos = []

class Lavagens(Enum):
    SIMPLES = "Lavagem Simples"
    COMPLETA = "Lavagem Completa"
    HIGIENIZACAO = "Higienização Interna"
    POLIMENTO = "Polimento (Veiculo Completo)"

class Servicos(Enum):
    CADASTRARSERV = "Cadastrar Serviço"
    EDITARSERV = "Editar Serviço"
    REMOVERSERV = "Remover Serviço"
    MOSTRARSERV = "Mostrar Serviço"
    CONCLUIRSERV = "Concluir Serviço"
    SAIR = "Sair"

while True:
    menu = choice(
        message="=====menu=====\nescolhe o que quer fazer:",
        options=[
            (Servicos.CADASTRARSERV, "Cadastrar Serviço"),
            (Servicos.EDITARSERV, "Editar Serviço"),
            (Servicos.REMOVERSERV, "Remover Serviço"),
            (Servicos.MOSTRARSERV, "Mostrar Serviço"),
            (Servicos.CONCLUIRSERV, "Concluir Serviço"),
            (Servicos.SAIR, "Sair"),
        ],
    )

    if menu == Servicos.CADASTRARSERV:
        servico = []

        nome = input("nome do cliente: ")
        servico.append(nome)

        cpf = input("cpf (somente numeros): ")
        while not (cpf.isdigit() and len(cpf) == 11):
            cpf = input("cpf invalido, necessita ter 11 numeros: ")
        servico.append(cpf)

        telefone = input("telefone (somente numeros): ")
        while not telefone.isdigit():
            telefone = input("telefone invalido, digite novamente: ")
        servico.append(telefone)

        placa = input("placa do carro: ")
        servico.append(placa)

        modelo = input("modelo do carro: ")
        servico.append(modelo)

        tipo = choice(
            message="tipo de lavagem:",
            options=[
                (Lavagens.SIMPLES, "Lavagem Externa"),
                (Lavagens.COMPLETA, "Lavagem Interna, Externa e Cera"),
                (Lavagens.HIGIENIZACAO, "Higienização Interna"),
                (Lavagens.POLIMENTO, "Polimento"),
            ],
        )
        servico.append(tipo)

        if tipo == Lavagens.SIMPLES:
            preco = "30"
        elif tipo == Lavagens.COMPLETA:
            preco = "50"
        elif tipo == Lavagens.HIGIENIZACAO:
            preco = "80"
        else:
            preco = "150"

        servico.append(preco)

        data = datetime.now().strftime("%d/%m/%Y %H:%M")
        servico.append(data)

        lista.append(servico)
        print("serviço cadastrado!\n")

    elif menu == Servicos.EDITARSERV:
        if lista == []:
            print("nenhum serviço cadastrado")
        else:
            for servico in lista:
                print(f"cliente: {servico[0]}, modelo: {servico[4]}")

            nome_busca = input("digita o nome do cliente que quer editar: ")
            achado = None
            for servico in lista:
                if servico[0] == nome_busca:
                    achado = servico
                    break

            if achado == None:
                print("esse servico esse serviço nao foi encontrado")
            else:
                campo = choice(
                    message="qual campo quer editar:",
                    options=[
                        ("nome", "Nome"),
                        ("cpf", "CPF"),
                        ("telefone", "Telefone"),
                        ("placa", "Placa"),
                        ("modelo", "Modelo"),
                        ("lavagem", "Tipo de lavagem"),
                    ],
                )

                if campo == "nome":
                    achado[0] = input("novo nome: ")
                elif campo == "cpf":
                    novo = input("novo cpf (somente numeros): ")
                    while not (novo.isdigit() and len(novo) == 11):
                        novo = input("cpf invalido, digita dnv: ")
                    achado[1] = novo
                elif campo == "telefone":
                    achado[2] = input("novo telefone: ")
                elif campo == "placa":
                    achado[3] = input("nova placa: ")
                elif campo == "modelo":
                    achado[4] = input("novo modelo: ")
                elif campo == "lavagem":
                    tipo = choice(
                        message="novo tipo de lavagem:",
                        options=[
                            (Lavagens.SIMPLES, "Lavagem Externa"),
                            (Lavagens.COMPLETA, "Lavagem Interna, Externa e Cera"),
                            (Lavagens.HIGIENIZACAO, "Higienização Interna"),
                            (Lavagens.POLIMENTO, "Polimento"),
                        ],
                    )
                    achado[5] = tipo
                print("serviço atualizado")

    elif menu == Servicos.REMOVERSERV:
        if lista == []:
            print("nenhum serviço cadastrado")
        else:
            for servico in lista:
                print(f"cliente: {servico[0]}, modelo: {servico[4]}")

            nome_busca = input("digita o nome do cliente pra remover: ")
            nova_lista = []
            for servico in lista:
                if servico[0] != nome_busca:
                    nova_lista.append(servico)
            lista = nova_lista
            print("serviço removido")

    elif menu == Servicos.MOSTRARSERV:
        if lista == []:
            print("nenhum serviço pra mostrar")
        else:
            for servico in lista:
                print(f"cliente: {servico[0]}, cpf: {servico[1]}, tel: {servico[2]}, placa: {servico[3]}, modelo: {servico[4]}, tipo: {servico[5]}, valor: R${servico[6]}, data: {servico[7]}")

    elif menu == Servicos.CONCLUIRSERV:
        if lista == []:
            print("nenhum serviço cadastradn")
        else:
            for servico in lista:
                print(f"cliente: {servico[0]}, modelo: {servico[4]}")

            nome_busca = input("digita o nome do cliente que concluiu o serviço: ")
            nova_lista = []
            for servico in lista:
                if servico[0] == nome_busca:
                    concluidos.append(servico)
                else:
                    nova_lista.append(servico)
            lista = nova_lista
            print("serviço concluído e movido pra lista de concluidos")

    elif menu == Servicos.SAIR:
        break
