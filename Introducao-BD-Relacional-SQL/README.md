# Banco de Dados Relacionais - SQL

## Conceitos Introdutórios

Existem alguns tipos de bancos de dados:

* Relacionais/SQL
* Não Relacionais/NoSQL (Not OnlySQL)
* Orientado a Objetos
* Hierárquivo

Para gerenciar um banco de dados, usamos Sistemas Gerenciadores de Banco de Dados (SGBD), que devem ter as funcionalidades básicas de:

* C reate (Criação)
* R ead (Leitura)
* U pdate (Atualização)
* D elete (Exclusão)

As características fundamentais de um banco de dados relacional são:

* Relacionamento entre tabelas,
* Linguagem de Consulta Estruturada (SQL),
* Integridade referencial,
* Normalização de dados,
* Segurança,
* Flexibilidade e extensibilidade,
* Suporte a transações ACID

Onde ACID significa:

* Atomicidade: Todas as operações são executadas com sucesso ou nenhuma é executada
* Consistência: Garantia de que o BD sai de um estado consistente para outro estado consistente.
* Isolamento: Cada transação é executada de forma isolada sem interferir em outra transação.
* Durabilidade: Uma vez que a transação é confirmada (commited) ela é permanente.

SQL

O SQL é dividido em alguns tipos de declarações:

* DQL - Linguagem de Consulta de Dados
 * SELECT
* DML - Linguagem de Manipulação de Dados
 * INSERT, UPDATE, DELETE
* DDL - Linguagem de Definição de Dados
 * CREATE, ALTER, DROP
* DCL: Linguagem de Controle de Dados
 * GRANT, REVOKE
* DTL: Linguagem de Transação de Dados
 * BEGIN, COMMIT, ROLLBACK

[Referência - SQL](https://www.sqltutotial.org/)

## MER e DER

O **MER** (**Modelo Entidade-Relacionamento**) é um modelo conceitual que é representado através de diagramas chamados **Diagramas Entidade-Relacionamento (DER)**.

[Site para Desenvolver os Modelos](https://app.creately.com/)
[Criando Diagramas com IA](https://app.quickdatabasediagrams.com/)

* **Entidades**: São nomeadas com substantivos concretos ou abstratos que representem de forma clara a sua função dentro do domínio.
* **Atributos**: Características ou propriedades das entidades. Descrevem informações específicas sobre uma entidade.
* **Relacionamentos**: São nomeadas com verbos e representam as associações entre entidades, mostra como elas se relacionam entre sí.
* **Cardinalidade**: Indica a forma que uma entidade se relaciona com a outra, indicando o número máximo de instâncias que podemos ter de uma entidade associada a outra entidade. As cardinalidades são: 1:1, 1:N ou N:M.

## Modelagem de Dados Relacionais

Os dados podem variar muito entre os diversos SGBD, os mais comuns são:
* Integer (Inteiro)
* Decimal/Numeric (Decimal/Numérico)
* Character/Varchar (Caracter)
* Date/Time (Data/hora)
* Boolean (Booleano)
* Text (Texto longo)

## Chave Primária

As chaves primárias é um atributo ou conjunto de atributos que identifica de forma exclusiva cada registro de uma tabela. Ela serve para garantir a integridade dos dados pois impede a duplicação de registro e ajuda a recuperação de forma eficiente dessa informação.

* Identificador exclusivo,
* Não pode conter valores nulos,
* Uma tabela pode ter apenas uma chave primária

## Chave Estrangeira

É usada para estabelecer e manter a integridade dos dados entre tabelas relacionadas

* Pode ser nula (Registro órfão),
* É possível ter mais de uma (ou nenhuma) em uma tabela.

### CREATE TABLE

```sql
CREATE TABLE {{nome}}
    ({{coluna}} {{tipo}} {{opções}} COMMENT {{'Comentario'}});
```
Algumas opções para criar a tabela:

* Restrições de valor
    * NOT NULL
    * UNIQUE
    * DEFAULT
* Chaves primárias e estrangeiras
* Auto incremento

### Chave Primária

```sql
CREATE TABLE {{tabela}}
(id INT PRIMARY KEY AUTOINCREMENT, ...);
```

### Chave Estrangeira

```sql
CREATE TABLE {{tabela}} (
    id int PRIMARY KEY,
    chave_estrangeira INT,
    FOREING KEY (chave_estrangeira) REFERENCES {{outra_tabela}}(id)
    );
```

### INSERT

```sql
INSERT INTO
    {{nome-tabela}}
    ([coluna1, coluna2, ...]) -- Pode-se ocultar as colunas, mas os valores deverão estar em ordem.
VALUES
    ([valor-coluna1, valor-coluna2, ...])
```

### SELECT

```sql
SELECT {{lista_colunas}}
FROM tabela
WHERE {{condição}};
```

O **SELECT** possui os seguintes operadores:

* = (Igualdade),
* <> ou != (Diferente),
* <=, <, >, >= (Menor ou igual a, menor que, maior que, maior ou igual a),
* LIKE (comparação de padrões),
* IN (Pertence a uma lista de valores),
* BETWEEN (Dentro de um intervalo),
* AND (E, lógico)
* OR (Ou, lógico)

### UPDATE

```sql
UPDATE {{tabela}}
SET
    {{coluna_1}} = {{novo_valor_1}}
    {{coluna_2}} = {{nova_valor_2}}
WHERE
    {{condicao}};
```

### DELETE

```sql
DELETE FROM {{tabela}}
WHERE
    {{condição}};
```

### DROP TABLE

É usado para remover uma tabela existente de um banco de dados relacional. Esse comanndo exclui permanentemente a tabela

```sql
DROP TABLE {{tabela}}
```

### ALTER TABLE

É usada no SQL para modificar a estrutura de uma tabela existente em um banco de dados relacional. Esse comando permite:

* Adicionar, alterar ou excluir colunas,
* Modificar as restrições, índices,
* Renomear a tabela entre outras alterações

Abaixo, vamos ver os seguintes exemplos:

1) Alteração do tamanho de uma coluna (VARCHAR(50) --> varchar(150))
2) Alteração do nome de uma tabela (tbela_ --> tabela)
3) Alteração Da coluna **'id'** para ser 'PRIMARY KEY'
4) Alteração da coluna **id_** para ser 'FOREIGN KEY' de {{outra_tabela}}(id)
```sql
1) ALTER TABLE {{tabela}} MODIFY COLUMN {{nome_coluna}} VARCHAR(150)
2) ALTER TABLE {{tbela}} RENAME {{tabela}}
3) ALTER TABLE {{tabela}} MODIFY COLUMN id INT PRIMARY KEY;
4) ALTER TABLE {{tabela}}
    ADD CONSTRAINT {{nome_contraint}}
    FOREIGN KEY(id_)
    REFERENCES {{outra_tabela}}(id)
```

## CONSTRAINTS - RESTRIÇÕES

São responsáveis por manter a integridade referencial dos dados, por isso, existem algumas cláusulas na hora da criação das chaves estrangeiras, que vão causar efeitos na exclusão/alteração desses dados:

`ON DELETE` Especifica o que acontece com os registros dependentes quando um registro pai é excluído,
`ON UPDATE` Define o comportamento dos registros dependentes quando um registro pai é atualizado,
`CASCADE`  Replica a alteração do pai nos filhos, 
`SET NULL` Remove a integridade referencial, 
`SET DEFAULT` Atribui valor padrão aos registros que ficarem sem pai.
`RESTRICT`

## Normalização

### 1FN - Primeira Forma Normal

A primeira forma nomral estabelce que cada valor em uma tabela deve ser atômico, ou seja, indivisível. Nenhum campo deve conter múltiplos valores ou listas. Por exemplo, um campo endereço, que recebia o endereço completo de uma pessoa deve ser dividido:

* Rua,
* Número,
* Cidade,
* Estado,
* País,


### 2FN - Segunda Forma Normal

A 2FN estabelece que uma tabela deve estar na 1FN e que todos os atributos não chave devem depender totalmente da chave primária. Uma **dica** é: Se a tabela tem uma **chave primária simples** não existe a possibilidade de termos dependência parcial e portanto ela já se encontra na 2FN

### 3FN - Terceira Forma Normal

A 3FN estabelece que uma tabela deve estar na 2FN e que nenhuma coluna não-chave deve depender de outra coluna não chave, ou seja, imagina, mais uma vez, o campo endereço. Se tivermos cidade e estado, repare que teríamos que separar pois cidade depende de estado. 


## Consultas Avançadas

### JOIN : Junção

São usadas no SQL para combinar dados de duas ou mais tabelaas relacionadas, em uma única consulta. Os tipos de Joins são:

* INNER JOIN
* LEFT JOIN ou LEFT OUTER JOIN
* RIGHT JOIN ou RIGHT OUTER JOIN
* FULL JOIN ou FULL OUTER JOIN


#### INNER JOIN

Retorna apenas as linhas que têm correspondência em ambas as tabelas envolvidas na junção. A junção é feita com base em uma condição de igualdade especificada na cláusula **ON**. É comum usar as tabelas de PK e FK, mas pode ser feito com outras colunas.

```sql
SELECT ({colunas})
FROM {{tabela_1}}
INNER JOIN {{tabela_2}} ON {{tabela_1.coluna}} = {{tabela2.coluna}};
WHERE {{condição}}
```

#### LEFT JOIN

Retorna todas as linhas da tabela à esquerda da junção e as linhas correspondentes da tabela à direita. Se não houver correspondência, os valores da tabela à direita serão NULL.

```sql
SELECT ({colunas})
FROM {{tabela_1}}
LEFT JOIN {{tabela_2}} ON {{tabela_1.coluna}} = {{tabela2.coluna}};
WHERE {{condição}}
```

#### RIGHT JOIN

Retorna todas as linhas da tabela à direita da junção e as linhas correspondentes da tabela à esquerda. Se não houver correspondência, os valores da tabela à direita serão NULL.

```sql
SELECT ({colunas})
FROM {{tabela_1}}
RIGHT JOIN {{tabela_2}} ON {{tabela_1.coluna}} = {{tabela2.coluna}};
WHERE {{condição}}
```

#### FULL JOIN - Não são todos os SGBDs que trazem esse join.

Retorna todas as linhas de todas as tabelas envolvidas na junção, combinando-as com base em uma condição de igualdade. Se não houver correspondência, os valores ausentes serão NULL.

```sql
SELECT ({colunas})
FROM {{tabela_1}}
FULL JOIN {{tabela_2}} ON {{tabela_1.coluna}} = {{tabela2.coluna}};
WHERE {{condição}}
```

## Sub consulta

As sub consultas, ou consultas aninhadas, permitem realizar consultas mais complexas, onde usa-se o resultado de uma consulta como entrada para outra consulta. As sub consultas podem ser usadas em várias partes de uma consulta:

* SELECT,
* FROM,
* WHERE,
* HAVING,
* JOIN.

## Funções Agregadas e Agrupamento de Resultados

### Funções Agregadas ou Funções Agregadoras

São funções que realizam algum tipo de pré-processamento ou cálculo nas colunas retornando um único valor, exemplo:

* **COUNT**: Conta número de registros,
* **SUM**: Soma os valores de uma coluna numérica,
* **AVG**: Cálcula a média dos valores de uma coluna numérica,
* **MIN**: Retorna o valor mínimo de uma coluna,
* **MAX**: Retorna o valor máximo de uma coluna.

```sql
SELECT COUNT(*) as total FROM {{tabela}}
```

Ou, por exemplo, pegando a pessoa mais velha de uma tabela de usuários, que tem o campo 'data_nascimento':

```sql
SELECT MAX(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS MAIOR_IDADE
FROM usuarios
```

### Agrupamento de Resultados

O agrupamento de resultados é usado para que possamos dividir os resultados em grupos, de acordo com algum tipo de critério. É feito usando a cláusula **GROUP BY**

Por exemplo, imagina que tenhamos uma tabela de **reservas**, que contém o id da pessoa que reservou e o id do destino que a pessoa reservou. Podemos contar quantas reservas temos para cada destino da seguinte forma:

```sql
SELECT COUNT(*) as qtd_reservas, id_destino FROM reservas
GROUP BY id_destino;
```

### Ordenação de Resultados

Servem para trazer os resultados ordenados de alguma maneira, por exemplo, do maior valor para o menor valor. A ordenação é feita usando a cláusula **ORDER BY**, por padrão é ASC. Exemplo, do resultado acima, imagina que queiramos ordenar do destino que tem mais reserva para o que tem menos reservas:

```sql
SELECT COUNT(*) AS Qtd_reservas, id_destino FROM reservas
GROUP BY id_destino
ORDER BY qtd_reservas DESC;
```

O **ORDER BY** permite a ordenação por multiplos campos, isso é feito colocando-se vírgula seguindo do nome do outro campo, exemplo:

```sql
SELECT COUNT(*) AS Qtd_reservas, id_destino FROM reservas
GROUP BY id_destino
ORDER BY qtd_reservas DESC, id_destino DESC;
```


## Índices de Buscas

São estruturas de dados que aceleram as pesquisas e a recuperação de informações do BD, podem ser criados em uma ou em várias colunas. O SQL possui um comando para analisar a execução das queries:

```sql
EXPLAIN
    SELECT *
    FROM {{tabela}}
    ...
```
A cláusula **EXPLAIN** é responsável por retornar os dados da análise que ele fez da execução da query. Essa análise pode retornar os seguintes campos:

* **select_type**: "SIMPLE", "SUBQUERY", "JOIN"
* **table**: Qual/quais tabela(s) foi/foram utilizadaa(s) nessa consulta
* **type**: "ALL", "INDEX" - Se consultou a tabela inteira ou alguma tipo de índice
* **possible_keys**: Os índices possíveis que podem ser utilizados na operação,
* **key**: O índice utilizada na operação, se aplicável,
* **key_len**: O comprimento do índice utilizado,
* **ref**: As colunas ou constantes usadas para acessar o índice
* **rows**: Quantas linhas o banco precisou processar até achar o resultado.

A criação de **índices** é feita seguindo da seguinte maneira:

```sql
CREATE INDEX {{nome_index}} ON {{tabela}}(coluna_1, coluna_2, ...)
```

Geralmente atribui-se o nome do index como **idx_coluna**.

