
def menu ():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Criar Usuário
    [nc] Criar Conta
    [lc] Listar Contas
    [q] Sair

    => """

    return input(menu)

def depositar (saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")

    else:
        print("\n @@@ Operação falhou! O valor informado é inválido. @@@")
    
    return saldo, extrato

def sacar (valor, saldo, limite, extrato, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n === Operação realizada com sucesso! ===")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def mostrar_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario (usuarios):
    cpf = input("Informe seu cpf (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("@@@ Já existe um usuário com esse CPF! @@@")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco })
    
    print ("Usuário cadastrado com sucesso!")

def filtrar_usuario (cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta (agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print ("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia,"numero_conta": numero_conta, "usuario": usuario}
    
    print ("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas (contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("="*100)
        print(linha)

def main (): 
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar (saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            
            saldo, extrato = sacar (
                valor=valor,
                saldo=saldo,
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
                )

        elif opcao == "e":
            mostrar_extrato (saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main ()