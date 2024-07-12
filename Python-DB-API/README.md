# Banco de Dados - Python

A primeira etapa para trabalhar com um banco de dados é estabelecer uma conexão. Vamos fazer isso usando **Python DB API**. Vamos usar o **SQLite**. A DB API do Python funciona para todos os bancos de dados, sendo necessário apenas baixar e importar o conector correto, isso é dado pela [PEP 249](https://peps.python.org/pep-0249/). Aqui, fez-se a escolha pelo **sqlite** por ser o banco de dados que está na documentação oficial do Python: [sqlite3 - documentação](https://docs.python.org/3/library/sqlite3.html).


```python
import sqlite3
connection = sqlite.connect('meu_banco.db')
```


É comum usar **conn** ou **con** para se referir a conexão. Por motivos didáticos, vamos usar **conexao**. Outro ponto é que utiliza-se, no geral, a extensão **.db** ou **.sqlite**. Por fim, o comando de conexão, gera um arquivo na raíz da pasta. Para escolher outro lugar para o banco de dados, devemos repetir os passos já aprendidos:


```python
import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.db')
```

Para criar a tabela e executar as queries em SQL, precisamos instânciar o **cursor**:


```python
cursor = conn.cursor()
```


E enfim, as queries são executadas usando o método **execute("QUERY")**:


```python
cursor.execute('CREATE TABLE {{nome_tabela}} ({{coluna_1}} {{tipo}} {{opções}}')
```

## Criando uma tabela

Por exemplo, vamos criar a tabela **clientes** com:
* id tipo inteiro, Primary Key com Auto-incremento,
* nome tipo varchar de 100 caracteres e
* email tipo varchar de 100 caracteres


```python
cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")
```


## Inserindo valores

Vamos explorar duas formas de inserir valores no SQL via Pytho DB. A primeira forma funciona porem é mais insegura, devido ao risco de injeção de código, veja:

Imagina que queiramos adicionar o usuário 'Thiago' com email 'thiago@email.com':


```python
nome = "Thiago"
email= "thiago@email.com"
cursor.execute(f"INSERT INTO clientes (nome, email) VALUES ('{nome}','{email}')")
cursor.commit()
```


A segunda forma, a **forma mais segura**, é feita usando queries preparadas, da seguinte maneira:


```python
data = ("Thiago", "thiago@email.com")
cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", data)
cursor.commit()
```

Poderíamos passar, também, da seguinte forma:


```python
nome = "Thiago"
email = "thiago@email.com"
cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (nome, email))
conexao.commit()
```

Repare que os valores são substituídos nos sinais "?". Por fim, todas as queries só são de fato executadas no banco, depois do **commit()**.


## Atualização de registros


```python
data = ("Thiago", "thiago@email.com", id)
cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?", data)
conexao.commit()
```

## Deletando registros


```python
id = 1
data = (id,)
cursor.execute("DELETE FROM clientes WHERE id = ?", data)
conexao.commit()
```

## Operações em lote


Quando precisamos inserir muitos registros de uma vez, podemos usar o método **executemany()** e, em vez de passar uma tupla, passaremos uma **lista de tuplas**.

```python
dados = [("Usuario 1", "email_1@email.com"), ("Usuario 2", "email_2@email.com"), ("Usuario 3", "email_3@email.com")]
cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
conexao.commit()
```

## Consultando registros

### Consultas com único resulto


Para realizar consultas com um único resultado, usamos o método **fetchone()**. Esse método retorna o próximo registro na lista de resultados ou **None** se não houver mais resultados. Repare que esse comando vai no lugar do **execute()** e, por isso, ainda é necessário escrever a query de busca!


```python
cursor.execute("SELECT * FROM minha_tabela WHERE id = 1")
resultado = cursor.fetchone()
print(resultado)
```

### Consultas com multiplos resultados

Para realizar consultas com múltiplos resultados, usamos o método **fetchall()**. Ele retorna uma lista de registros ou uma lista vazia se não houver resultado.

```python
cursor.execute("SELECT * FROM minha_tabela")
resultado = cursor.fetchall()
for linha in resultado:
    print(linha)
```

Até agora, os resultados são retornados como tuplas por padrão. Se a tupla não atender as nossas necessidades podemos usar a classe **sqlite3.Row** ou uma **row_factory** customizada, vejamos um exemplo:

```python
cursor.row_factory = sqlite3.Row
cursor.execute("SELECT * FROM minha_tabela WHERE id = 1")
resultado = cursor.fetchone()
print(dict(result))
```

## Boas práticas em consultas SQL

* Evitar concatenação de strings nas consultas (evitar ataques de injeção SQL)
* Usar consultas parametrizadas

Vejamos um exemplo.

Imagina que temos a seguinte base:

|id|nome|email|
|--|----|--------|
|2| João | joao@email.com|
|3| Maria | maria@email.com|
|4| José | jose@email.com|
|5| Joana | joana@email.com|
|6| Ariel | ariel@email.com|

E imagina que fizemos o código usando a concatenação de strings, onde o usuário que insere o **id** para consultar o **nome** do **cliente**:

```python
import sqlite3

conexao = sqlite3.connect("banco_clientes.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

id_cliente = input("Informe o id do cliente: ")
cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}")

clientes = cursor.fetchall()

for cliente in clientes:
    print(dict(cliente))

```

Repare que um usuário normal faria consultas como:


```python
Informe o id do cliente: 
>>> 2
>>>{'id': 2, 'nome': 'João', 'email': 'joao@email.com'}
# Ou
Informe o id do cliente: 
>>> 1
>>>
```

Mas uma pessoa má intencionada faria uma injeção de código SQL:


```python
Informe o id do cliente: 
>>> 1 OR 1=1
>>>{'id': 2, 'nome': 'João', 'email': 'joao@email.com'}
>>>{'id': 3, 'nome': 'Maria', 'email': 'maria@email.com'}
>>>{'id': 4, 'nome': 'José', 'email': 'jose@email.com'}
>>>{'id': 5, 'nome': 'Joana', 'email': 'joana@email.com'}
>>>{'id': 6, 'nome': 'Ariel', 'email': 'ariel@email.com'}
```

Ou seja, a pessoa conseguiu realizar uma vazamento nos dados. Isso se deu porque, no final, o comando SQL executado foi:


```sql
SELECT * FROM clientes WHERE id = 1 OR 1=1
```

É facil ver que:
* 1=1 é sempre TRUE e 
* A OR TRUE é sempre TRUE.

Repare que usar consultas parametrizadas resolve esse problema pois:

```python
id_cliente = input("Informe o id do cliente: ")
cursor.execute(f"SELECT * FROM clientes WHERE id=?", (id_cliente,))

clientes = cursor.fetchall()

for cliente in clientes:
    print(dict(cliente))
```

Caso seja injetado SQL, resultará na seguinte consulta:

```sql
SELECT * FROM clientes WHERE id = (1 OR 1=1)
```

Onde 
```sql
SELECT * FROM clientes WHERE id = TRUE
```

## Gerenciando transações

A DB API também nos permite gerenciar transações, o que é crucial para manter a integridade dos dados. Para isso, precisa-se criar uma estrutura **try-except**. Vamos supor que vamos fazer 'n' queries mas uma delas vai ter erro. Se não tratarmos, todas as queries executadas até a query de erro, será persistida no banco, quando o correto é ou persistir todas as queries ou nenhuma:

```python
try:
    cursor.execute("QUERY_1")
    cursor.execute("QUERY_2")
    cursor.execute("QUERY_3")
    ... # Aqui tem alguma query com erro!
    cursor.execute("QUERY_n")
    conexao.commit()
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    conexao.rollback()
```

Dessa forma, quando for executada a query com alguma incosistencia, a exceção será levantada e tudo será desfeito (rollback()). Alguns conectores possuem o bloco **with** como usamos com arquivos.