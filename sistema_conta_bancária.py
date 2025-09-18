conta = {
    "saldo": 0,
    "limite": 500,
    "extrato": "",
    "numero_saques": 0,
    "limite_saques": 3
    }


def deposito(conta, valor):
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ +{valor:.2f}\n"
        print(f"\n-----------------------\nDepósito de R$ {valor:.2f} realizado com sucesso!\n-----------------------")
    else:
        print("\n-----------------------\nValor inválido para depósito.\n-----------------------")

def sacar(conta, valor):
    if conta["numero_saques"] >= conta["limite_saques"]:
        print("-----------------------\nLimite de saques diários atingido!\n-----------------------")
    elif valor > conta["saldo"]:
        print("-----------------------\nSaldo insuficiente!\n-----------------------")
    elif valor > conta["limite"]:
        print("-----------------------\nValor excede o limite de R$ 500.00!\n-----------------------")
    elif valor <= 0:
        print("-----------------------\nValor inválido para saque!\n-----------------------")
    else:
        conta["saldo"] -= valor
        conta["numero_saques"] += 1
        conta["extrato"] += f"Saque:    R$ -{valor:.2f}\n"
        print(f"\n-----------------------\nSaque de R$ {valor:.2f} realizado com sucesso!\n-----------------------")

def extrato_bancario(conta):
    print("\n--------EXTRATO--------")
    print(conta["extrato"] if conta["extrato"] else "Não foram realizadas movimentações.\n")
    print(f"Saldo atual: R$ {conta["saldo"]:.2f}")
    print("-----------------------\n")

while True:
    menu = f"""
---------MENU----------
Saldo: R$ {conta["saldo"]:.2f}

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair
-----------------------

Selecione a operação desejada: """
    opcao = input(menu).strip().lower()

    if opcao == "d":
        valor = float(input("\nInforme o valor do depósito: R$ "))
        deposito(conta, valor)

    elif opcao == "s":
        valor = float(input(
            f"\n---------SAQUE---------\n"
            f"Saldo Disponível: R$ {conta["saldo"]:.2f}\n"
            f"Limite Disponível: R$ {conta["limite"]:.2f}\n"
            f"Saques Disponíveis: {conta["numero_saques"]}/{conta["limite_saques"]}\n"
            f"-----------------------\n"
            f"\nInforme o valor do saque: R$ "
        ))
        sacar(conta, valor)

    elif opcao == "e":
        extrato_bancario(conta)

    elif opcao == "q":
        print("\n-----------------------\nSaindo do sistema, obrigado!\n-----------------------\n")
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")