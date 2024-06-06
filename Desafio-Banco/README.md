### Desafio 1

No desafio 1, cria-se um sistema bancário simples que deve possuir:  
* Saque,  
* Depósito,  
* Visualizar extrato.  

O Saque:  

* Limite de 3 saques diários com valor máximo de R$ 500,00/saque
* Se o usuário não tiver saldo em conta, não pode fazer o saque.

Depósito:  

* Valores positivos.

Todas as operações (Saque e Depósito) devem ser armazenados em uma variável e devem ser exibidos na operação extrato.

Deve-se utilizar o modelo dado.


### Desafio 2

No desafio 2 deve-se otimizar o sistema bancário, deixando-o mais modularizado, através da utilização de funções.

Nesse desafio deve-se:  
1. Criar as funções:  
1.1 Sacar,  
1.2 Depositar  
1.3 Visualizar histórico,  
2. Criar duas novas funções:  
2.1 Criar usuário,  
2.2 Criar conta corrente.

As regras são:

Função sacar deve ser **keyword only**,  
Deve ter:
* saldo, 
* valor, 
* extrato,
* limite, 
* numero de saques, 
* limite de saques.    
Retorna: saldo e extrato

Função depositar deve ser **positional only**,  
Deve ter: 
* saldo, 
* valor,  
* extrato.  
Retorna: saldo e extrato.  

Função extrato deve ser **positional only e keyword only**,  
Positional only: 
* saldo,  



Função criar usuário:  
Deve armazenar os usuários em uma lista,  
Usuário deve ter: 
* nome, 
* data de nascimento, 
* cpf (apenas números), 
* logradouro (logradouro, nro - bairro - cidade/UF), 
* Não deve armazenar 2 cpfs iguais.

Função criar conta
Deve armazenar contas em uma lista,  
conta deve ter: 
* agencia, 
* numero da conta, 
* usuario. 
* A conta é sequencial inciando em 1, 
* Agencia é fixa (0001), 
* Usuário pode ter mais de uma conta mas uma conta pode ser de apenas um usuário.  
