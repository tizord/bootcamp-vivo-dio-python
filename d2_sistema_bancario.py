'''
Bootcamp - Vivo - Python AI Backend Developer

Desafio 2 - Otimizar o sistema bancário

'''

def sacar(*,saldo:float, valor:float, limite:float, numero_saques:int, limite_saques:int):

    """
    Função sacar.

    Essa função efetua saque de uma conta corrente.

    Args:
        saldo (float): O saldo atual na conta corrente,
        valor (float): O valor a ser sacado da conta corrente,
        limite (float): O valor limite que se pode sacar dessa conta,
        numero_saques (int): Quantidade de saques efetuada pelo cliente,
        limite_saques (int): Quantidade máxima de saques que o cliente pode efetuar.
    
    """

    if valor > saldo:
        return f"O saque não pôde ser feito. Seu saldo é de R$ {saldo}"
    elif valor > limite:
        return f"O saque não pôde ser feito. O seu limite para saques é de R$ {limite}"
    elif numero_saques > limite_saques:
        return f"O saque não pôde ser feito, você já atingiu sua quantidade de saques diários."
    else:
        saldo -= valor
        numero_saques += 1
        
    return saldo

def depositar(saldo:float, valor:float, /):

    """
    Função Depositar.

    Essa função efetua depositos de uma conta corrente.

    Args:
        saldo (float): O saldo atual na conta corrente,
        valor (float): O valor a ser depositado na conta corrente,

    
    """
 
    saldo += valor    
    return saldo