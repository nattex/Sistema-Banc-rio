livro = "leitura do livro até o último capitulo"

def menu():
    print(" ================= Menu =================")
    print("1. Depositar")
    print("2. Saque")
    print("3. Extrato")
    print("4. Saldo")
    print("5. Sair")
    print(" ========================================")


def depositar(saldo,extrato):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Valor do deposito: {valor:.2f}\n"

    return saldo, extrato


def sacar(saldo,extrato):
    valor = float(input("Informe o valor que deseja sacar: "))
    
    if valor > 0 and valor <= saldo:
        saldo -= valor
        extrato += f"Valor do saque: {valor:.2f}"
        
    elif valor > saldo:
        print("Saldo Negativo! Não foi possível sacar.")

    return saldo, extrato


def exibir_extrato(extrato):
    print(extrato if extrato  else "Não foi realizado movimentações")

    return extrato


def exibir_total(saldo):
    print("Seu saldo:",saldo if saldo else "Seu saldo está negativo")



def main():

    saldo = 0
    extrato = ""

    while True:
        menu()
        
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            saldo, extrato = depositar(saldo,extrato)
        elif opcao == "2":
            saldo, extrato = sacar(saldo,extrato)
        elif opcao == "3":
            extrato = exibir_extrato(extrato)
        elif opcao == "4":
            saldo = exibir_total(saldo)
        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if livro == "leitura do livro até o último capitulo":
    saldo = 0 
    extrato = ""
    main()

