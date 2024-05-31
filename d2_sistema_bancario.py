'''
Bootcamp - Vivo - Python AI Backend Developer

Desafio 2 - Otimizar o sistema bancário

'''

# VARIAVEIS GLOBAIS



MENU = """
### MENU ###

[d] - Depósito
[s] - Sacar
[e] - Extrato
[cr] - Criar correntista
[cc] - Criar conta
[lc] - Listas contas
[q] - Sair


>>
"""

def menu(opcoes = MENU):

    SALDO = 0
    LIMITE = 500
    EXTRATO = "### EXTRATO BANCARIO ###"
    numero_saques = 0
    LIMITE_SAQUE = 5
    contas = []
    correntistas = []

    while True:
        print(MENU)
        opcao = input("Insira a opção desejada \n").lower()


        if opcao == 'd':
            print('\n\nFunção Depósito')
            deposito = float(input('Insira o valor a ser depositado: \n'))
            SALDO, EXTRATO = depositar(SALDO, deposito, EXTRATO)
            print('Transação concluída')

        elif opcao == 'e':
            print('\n\nFunção Extrato')
            visualizar_historico(SALDO, extrato=EXTRATO)


        elif opcao == 's':
            print('\n\nFunção Saque')
            saque = float(input('Insira o valor a ser sacado: \n'))
            SALDO, EXTRATO = sacar(saldo=SALDO, valor=saque, limite=LIMITE, numero_saques=numero_saques, limite_saques=LIMITE_SAQUE, extrato=EXTRATO)

        elif opcao == 'cr':
            print('\n\nFunção Criar correntista')
            criar_correntista(correntistas)

        elif opcao == 'cc':
            print('\n\nFunção Criar conta')
            n_conta = len(contas) + 1
            criar_conta(n_conta, correntistas, contas)

        elif opcao == 'lc':
            print('\n\nFunção Listar contas')
            lista_contas = listar_contas(contas)
            print(lista_contas)            
        elif opcao == 'q':
            print('Operação finalizada')
            break

        else:
            print('Operação inválida, por favor selecione uma operação válida')

def sacar(*,saldo:float, valor:float, limite:float, numero_saques:int, limite_saques:int, extrato):

    """
    Função sacar.

    Essa função efetua saque de uma conta corrente.

    Args:
        saldo (float): O saldo atual na conta corrente,
        valor (float): O valor a ser sacado da conta corrente,
        limite (float): O valor limite que se pode sacar dessa conta,
        numero_saques (int): Quantidade de saques efetuada pelo cliente,
        limite_saques (int): Quantidade máxima de saques que o cliente pode efetuar.
        extrato (str): Exibe o extrato da conta
    
    """
    if numero_saques > limite_saques:
        return f"O saque não pôde ser feito, você já atingiu sua quantidade de saques diários."
    elif valor > saldo:
        return f"O saque não pôde ser feito. Seu saldo é de R$ {saldo}"
    elif valor > limite:
        return f"O saque não pôde ser feito. O seu limite para saques é de R$ {limite}"
    
    else:
        saldo -= valor
        numero_saques -= 1
        extrato += f'\n- R$ {valor}'
        
    return saldo, extrato

def depositar(saldo:float, valor:float, extrato:str, /):

    """
    Função Depositar.

    Essa função efetua depositos de uma conta corrente.

    Args:
        saldo (float): O saldo atual na conta corrente,
        valor (float): O valor a ser depositado na conta corrente,
        extrato (str): Exibe o extrato da conta
    
    """
 
    saldo += valor
    extrato += f'\n+ R$ {valor}'

    return saldo, extrato

def visualizar_historico(saldo, /, *, extrato):
    """
    Função visualizar histórico
    
    Args:
        saldo (float): O saldo atual na conta corrente,
        extrato (str): Função extrato com o extrato da conta

    
    """

    print(f"{5*'-'} EXTRATO {5*'-'}")
    print(extrato)
    print(f"\n Saldo: {saldo}")

def criar_correntista(correntistas: list):
    """
    * nome, 
    * data de nascimento, 
    * cpf (apenas números), 
    * logradouro (logradouro, nro - bairro - cidade/UF), 
    * Não deve armazenar 2 cpfs iguais.
    """
    cpf = input("Insira o CPF (somente números): ")
    
    existe_correntista = filtrar_correntista(cpf, correntistas)
    if existe_correntista:
        print("Esse correntista já existe!")
    else:
        nome = input("Insira o nome completo: ")
        data_nascimento = input("Insira a data de nascimento (dd/mm/aaaa): ")
        endereco = input("Insira o endereço completo: (logradouro, número, bairro, cidade, sigla UF): ")
        correntistas.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})
        print(f'O correntista {cpf} - {nome} foi criado com sucesso!')

def filtrar_correntista(cpf, correntistas):
    correntista_filtrado = [correntista for correntista in correntistas if correntista["cpf"] == cpf]
    return correntista_filtrado[0] if correntista_filtrado else None


def criar_conta(n_conta: int, correntistas: list, contas:list):
    
    agencia = '0001'
    cpf = input("Insira o CPF (somente números): ")
    correntista = filtrar_correntista(cpf, correntistas)

    if correntista:
        contas.append({"agencia": agencia, "numero_conta": n_conta, "correntista": correntista})
        print(f"Conta criada com sucesso!\nAgencia - Conta: {agencia} - {n_conta}")
    else:
        print ("\n\nCorrentista não encontrado")

    return contas

def listar_contas(contas: list):

    return contas

def main():
    menu()

__init__ = main()