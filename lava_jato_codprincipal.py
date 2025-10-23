from prompt_toolkit.shortcuts import choice
from enum import Enum
from datetime import datetime

lista = []
menu = None
print(lista)

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

# FUNÇÕES 
def selecionar_lavagem():
    tipolavagem = choice(
        message="Digite o tipo de lavagem:",
        options=[
            (Lavagens.SIMPLES, "Lavagem Externa"),
            (Lavagens.COMPLETA, "Lavagem Interna, Externa e Cera"),
            (Lavagens.HIGIENIZACAO, "Higienização Interna"),
            (Lavagens.POLIMENTO, "Polimento"),
        ],
    )

    lista.append(tipolavagem)
    if tipolavagem == Lavagens.SIMPLES:
        preco = "30"
    elif tipolavagem == Lavagens.COMPLETA:
        preco = "50"
    elif tipolavagem == Lavagens.HIGIENIZACAO:
        preco = "80"
    else:
        preco = "150"

    print(f"Valor da Lavagem {tipolavagem.value}: R$ {preco}")
    lista.append(preco)


def cadastrar_servico():
    nome = input("Digite o nome do cliente: ")
    lista.append(nome)

    while True:
        cpf = input("Digite o CPF (somente números): ")
        if cpf.isdigit() and len(cpf) == 11:
            lista.append(cpf)
            break
        else:
            print("CPF inválido. Digite 11 números sem pontos.")

    while True:
        telefone = input("Digite o telefone (somente números): ")
        if telefone.isdigit():
            lista.append(telefone)
            break
        else:
            print("Telefone inválido, digite apenas números.")

    placa = input("Digite a placa do carro: ")
    lista.append(placa)

    modelo = input("Digite o modelo do carro: ")
    lista.append(modelo)

    selecionar_lavagem()
    data_feita = datetime.now().strftime("%d/%m/%Y %H:%M")
    lista.append(data_feita)
    print("\nServiço cadastrado com sucesso!")
    print("Informações salvas:", lista)


def editar_servico():
    if not lista:
        print("Nenhum serviço cadastrado.")
    else:
        print("Serviço atual:", lista)
        campo = choice(
            message=("Qual campo deseja editar?"),
            options=[
                ("nome", "Nome"),
                ("cpf", "CPF"),
                ("telefone", "Telefone"),
                ("placa", "Placa"),
                ("modelo", "Modelo do carro"),
                ("lavagem", "Tipo de serviço"),
                ("voltar", "Voltar"),
            ],
        )
        if campo == "nome":
            lista[0] = input("Novo nome: ")
        elif campo == "cpf":
            while True:
                novo_cpf = input("Novo CPF (somente números): ")
                if novo_cpf.isdigit() and len(novo_cpf) == 11:
                    lista[1] = novo_cpf
                    break
                else:
                    print("CPF inválido.")
        elif campo == "telefone":
            lista[2] = input("Novo telefone: ")
        elif campo == "placa":
            lista[3] = input("Nova placa: ")
        elif campo == "modelo":
            lista[4] = input("Novo modelo: ")
        elif campo == "lavagem":
            selecionar_lavagem()

        print("Serviço atualizado:", lista)


def menu_principal():
    while True:
        menu = choice(
            message="=====MENU=====\nSelecione o Serviço Desejado:",
            options=[
                (Servicos.CADASTRARSERV, "Cadastrar Serviço"),
                (Servicos.EDITARSERV, "Editar Serviço"),
                (Servicos.REMOVERSERV, "Remover Serviço"),
                (Servicos.MOSTRARSERV, "Mostrar Serviço"),
                (Servicos.CONCLUIRSERV, "Concluir Serviço"),
                (Servicos.SAIR, "Sair do Menu"),
            ],
        )

        if menu == Servicos.CADASTRARSERV:
            cadastrar_servico()
        elif menu == Servicos.EDITARSERV:
            editar_servico()
        elif menu == Servicos.SAIR:
            break


menu_principal()