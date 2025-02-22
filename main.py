from datetime import datetime
import pytz

senha_padrao = "1234"
saldo = 0.0
extrato = []

def data_hora():
    """ Retorna a data e hora atual no fuso horário de Brasília. """

    fuso_brasilia = pytz.timezone("America/Sao_Paulo")
    data_hora_brasil = datetime.now(fuso_brasilia)
    return data_hora_brasil.strftime("%d/%m/%Y %H:%M:%S")

def ver_saldo():
    """ Retorna o saldo formatado. """

    return f"Seu saldo: R$ {saldo:.2f} - {data_hora()}"

def deposito():
    """ Realiza um depósito na conta. """

    global saldo

    valor_deposito = float(input("Informe o valor do deposito : "))

    if valor_deposito > 0:
        saldo += valor_deposito
        extrato.append(f"Depósito de R$ {valor_deposito:.2f} em {data_hora()}")
        print(f"Depósito realizado com sucesso. Seu saldo atual é R$ {saldo:.2f}.")
    else:
        print("Erro: O valor é insuficiente.")


def saque():
    """ Realiza um saque, se o saldo for suficiente. """

    global saldo

    valor_saque = float(input("Informe o valor do saque: "))

    if valor_saque > 0 and valor_saque <= saldo:
        saldo -= valor_saque
        extrato.append(f"Saque de R$ {valor_saque:.2f} em {data_hora()}")
        print(f"Saque realizado com sucesso. Seu saldo atual é R$ {saldo:.2f}.")
        print("\n")
    else:
        print("\nErro: Saldo insuficiente ou valor inválido.")

def exibir_extrato():
    """ Exibe todas as movimentações da conta. """

    if not extrato:
        print("Nenhuma movimentação realizada.")

    else:
        for tipo in extrato:
          print(f"Extrato das movimentações: R${tipo}")




''' Menu Principal'''
while True:
    print("\n=== Caixa Eletrônico ===")
    print("\n1. Depositar\n2. Sacar\n3. Ver Saldo\n4. Extrato\n5. Sair")


    opcao = input("Escolha uma opção: ")
    tentativas=3

    while tentativas>0: #Validação da Senha
      if input("Digite sua senha: ") == senha_padrao:
          print("\nSenha correta. Acesso permitido.")
          break

      tentativas-=1
      print(f"\nSenha incorreta! Tentativas Restantes: {tentativas}")

    if tentativas ==0:
      print("Conta Bloqueada!")
      break


    '''  Menu Interativo  '''

    if opcao == "1":
        deposito()
    elif opcao == "2":
        saque()
    elif opcao == "3":
        print(ver_saldo())
    elif opcao == "4":
        exibir_extrato()
    elif opcao == "5":
        print(f"\nOperações finalizadas. Seu saldo final é R$ {saldo:.2f}.")
        break
    else:
        print("Opção inválida. Escolha novamente.")
