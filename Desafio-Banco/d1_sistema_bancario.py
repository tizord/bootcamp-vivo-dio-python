'''
Bootcamp - Vivo - Python AI Backend Developer

Desafio 1 - Criar um sistema bancário, com 3 operações básicas:

Saque,
Depósito e
Visualizar extrato

Por enquanto, só existe 1 correntista.

O Saque:

    Limite de 3 saques diários com valor máximo de R$ 500,00/saque
    Se o usuário não tiver saldo em conta, não pode fazer o saque.

Depósito:

    Valores positivos.

Todas as operações (Saque e Depósito) devem ser armazenados em uma variável
    e devem ser exibidos na operação extrato.

Deve-se utilizar o modelo dado

'''

menu = """
### MENU ###

[d] - Depósito
[s] - Sacar
[e] - Extrato
[q] - Sair


>>
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 5

while True:

    opcao = input(menu).lower()


    if opcao == 'd':
        print('\n\nDepósito')
        deposito = float(input('Insira o valor a ser depositado: \n'))
        saldo += deposito
        print('Transação concluída')

    elif opcao == 'e':
        print('\n\nExtrato')
        print(f'O seu saldo é de R$ {saldo:.2f}')

    elif opcao == 's':
        print('\n\nSaque')
        saque = float(input('Insira o valor a ser sacado: \n'))
        if saque > saldo:
            print('Você não possui dinheiro suficiente para essa transação')
            print('Transação cancelada')
        else:
            saldo -= saque
            print('Transação concluída')

    elif opcao == 'q':
        print('Operação finalizada')
        break

    else:
        print('Operação inválida, por favor selecione uma operação válida')