# Banco de Dados Não Relacional (NoSQL)

O termo correto é **NOT Only SQL**, ou seja, não **apenas** SQL. A ideia é que esse tipo de banco de dados seja mais abrangente, eles não seguem modelo de tabelas e relacionamentos. São projetados para lidar com **alto volume de dados**, alta escalabilidade. Os BD relacionais só possuem escalabilidade vertical, ou seja, mencessita mais hardware ao passo que o BD NoSQL possui escalabilidade lateral. Além disso os BD NoSQL possuem alta **flexibilidade** na estrutura de dados. Eles são amplamente utilizados em cenários onde a consistência imediata dos dados não é crítica.

As **vantagens** dos bancos NoSQL são:

* Flexibilidade na modelagem,
* Alta escalabilidade,
* Melhor desempenho em cenário de consulta intensiva,
* Tolerância a falhas

As **desvantagens** são:

* Menor consistência de dados imediata,
* Menor suporte a consultas complexas -> depende do SGBD


## Diferenças

| SQL | NoSQL |
|-----|-------|
|Modelo de dados fixo| Modelo de dados flexível|
|Escalabilidade vertical (hardware)|Escalabilidade horizontal|
|Transações ACID 100%|Transações ACID ausentes total ou parcial|
|Linguagem de consulta SQL|Cada SGBD tem sua própria|


Um link útil para entender melhor o que são banco de dados não-relacionais pode ser visto [aqui](https://www.oracle.com/br/database/nosql/what-is-nosql/)


## Visão Geral dos tipos NoSQL

Os banco de dados NoSQL são divididos de acordo com seu tipo de armazenamento. Alguns dos principais tipos são:

* Key-Value,
* Documento,
* Coluna,
* Grafos,
* etc

### Key-Value - Chave Valor

Armazena dados como pares de chave e valor, onde cada chave é um identificaor único para acessar o valor correspondente. Alta escalabilidade horizontal, pode ser facilmente distribuído em varios servidores e tem o acesso a informação muito rápido, por ser feito com base em chave e por ser armazenado em memória. Possui sistema de armazenamento simples.  
**Exemplo de SGBD**: Redis, Riak, Amazon DynamoDB.  
**Uso**: Um site pode usar um BD Redis para armazenar informações de sessão do usuário.

### Documento

Armazenam dados em documentos semiestruturados, geralmente em formato JSON ou BSON. Mas não é regra, pode armazenar em XML por exemplo. Possui flexibilidade de schema, não requer qualquer uso de estrutura rígida, permite edição do schema, como remoção ou adição de campo, facilmente de acordo com seu documento, pois esses documentos não tem qualquer restrição dos tipos de informação que são ali inseridos, podendo ter informações de diferentes estruturas. Tem modelagem de dados complexa e possui consultas eficientes.   
**Exemplo de SGBD**: MongoDB, Couchbase, Apache CouchDB.  
**Uso**: Um catálogo de e-commerce pode usar o MongoDB para armazenar informações de produtos como: nome, descrição, preço e atributos adicionais.


### Coluna

Armazena dados em formato de colunas, o que permite alta escalabilidade e eficiência em determinados tipos de consultas. Possui escalabilidade horizontal muito boa, recuperação de dados é extremamente eficiente e tem schema flexível.  
**Exemplo de SGBD**: Apache Cassandra, ScyllaDB, HBase.  
**Uso**: Um sistema de registro de aplicativos pode usar o Apache Cassandra para armazenar registros de log.


### Grafo

Armazena e consulta dados interconectados, onde os relacionamentos entre os dados são tão importantes quanto os próprios dados.  
**Exemplo de SGBD**: Neo4j, Amazon Neptune, JanusGraph.  
**Uso**: Uma rede social pode usar o Neo4j para armazenar os perfil dos usuários e suas conexões, permitindo consultas eficientes para encontrar amigos em comum.  


## Introdução ao MongoDB

O MongoDB pe um banco de dados NoSQL orientado a documentos, ele lida bem com grande volumes de dados e possui alta escalabilidade horizontal e modelagem flexível. O MongoDB não exige um esquema e permite que os dados sejam armazenados em formato BSON (Binary JSON), proporcionando uma estrutura semiestruturada.

**Vantagens**

* Flexibilidade na modelagem de dados,
* Escalabilidade horizontal para lidar com grandes volumes de dados,
* Consultas ricas e suporte a consultas complexas,
* Alta disponibilidade e tolerância a falhas,
* Comunidade ativa e recusos de suporte.

**Desvantagens**

* Menor consistência imediata em comparação com bancos de dados relacionais,
* Consultas complexas podem exigir um maior conhecimento e planejamento adequado,
* Maior consumo de espaço de armazenamento em comparação com bancos de dados relacionais devido à flexibilidade dos documentos.

**Onde é usado**

* Aplicações web,
* Análise de big data,
* Armazenamento de dados semiestruturados
* Casos de uso de geolocalização

[Documentação MongoDB](https://www.mongodb.com/docs/manual/introduction/)


## Modelagem de dados usando Documentos

A estrutura do MongoDB.

* Um Databse é composto por várias coleções,
* Uma coleção é composta por vários documentos,
* Não existe um documento fora de uma coleção.

![alt text](image.png)

### Coleções

É um agrupamento lógico de documentos, não existe esquema ou que os documentos tenham a mesma estrutura, ou seja, dentro de uma coleção podemos ter documentos com campos a mais ou a menos. Mas no geral, a ideia é, dentro de uma coleção, ter documentos relacionados. Os documentos tem as seguintes características:

* Os nomes das coleções devem seguir algumas regras:
    * Devem começar com uma letra ou um underscore (_),
    * Podem conter letras, número ou underscores,
    * Não podem ser vazios,
    * Não é recomendado usar caractéres especiais,
    * Não podem ter mais de 64 bytes de comprimento.

### Documentos

É a representação da informação que estamos salvando, análogo ao registro ou a tupla. São armazenados em documentos BSON (Binary JSON), que são estruturas flexíveis e semiestruturadas, cada documento possui um identificador único chamado **"_id"** e é composto por pares de chaves e valores. Os documentos tem as seguintes características:

* Tamanho máximo, cada documento pode ter tamanho máximo de 16 MB,
* Aninhamento de documentos (inner document),
* Flexibilidade na evolução do esquema.

O mongoDB tem os seguintes **tipos de dados simples**:

* **String**,
* **Number**,
* **Boolen**,
* **Date**,
* **Null**,
* **ObjectId**

E tem os seuintes **tipos de dados complexos**:

* **Array**,
* **Documento Embutido (Embedded Document)**,
* **Referência (Reference)**,
* **GeoJSON**.

## Estrutura de um documento

Esse documento é um documento simples:


```mongodb
{
    _id: ObjectId(""),
    "nome_campo": "valor_campo",
    ...
}
```

[Formatador JSON](https://jsonformatter.curiousconcept.com/)

## Estratégia de Modelagem de Dados Eficientes e Escaláveis

### Modelagem orientada por consultas

A modelagem de dados no MongoDB deve ser orientada pelas consultas que serão realizadas com mais frequência.

#### Modelagem com estratégia desnormalizada

**Inner Documents**: No MongoDB é comum **denormalziar** os dados para evitar operações de junção (join) custosas. Isso significa que os dados relacionados podem ser armazenados junto em um único documento, em vez de serem distribuídos em várias coleções.

Quando usar **estratégia desnormalizada**?
* Os dados aninhados são específicos para o documento pai, ou seja, sem o pai os dados não existem;
* Os dados aninhados são sempre acessados juntamente com o documento pai;
* A cardinalidade do relacionamento é 1:N

Quando **não** utilizar os **estratégia desnormalizada**?
* Se os dados aninhados precisarem ser consultados e atualizados independentemente do documento pai, é mais adequado utilizar coleções separadas

#### Modelagem com estratégia de referência

Quando usar **estratégia de referência**?
* Os dados tem seu próprio significado e podem ser acessados independentemente do documento pai;
* Os dados têm uma cardinalidade mais alta;

Quando **não** utilizar os **inner documents**?
* Se os dados aninhados precisarem ser consultados e atualizados independentemente do documento pai, é mais adequado utilizar coleções separadas


[Padrões para modelagem de dados em MongoDB](https://www.luiztools.com.br/post/padroes-para-modelagem-de-dados-documentos-em-mongodb/)

## Operações no MongoDB

### Criando um DataBase

```mongodb
use {{nome_do_banco}}
```
Se o banco não existir, ele irá criar, se o banco existir ele irá selecionar o banco.  
Enquanto o Database não tiver uma collection ele não será apresentado na lista.

### Criando uma collection

```mongodb
db.createCollection("nome_colecao")
```

### Inserindo Documentos

```mongodb
db.nome_colecao.insertOne({})
db.nome_colecao.insertMany([{}])
```

### Consultando Documentos

```mongodb
db.nome_colecao.find({}) // Dessa forma é similar ao SELECT * FROM tabela
db.nome_colecao.findOne({});
db.nome_colecao.findOneAndUpdate({},{});
db.nome_colecao.findOneAndDelete({});
```

Nas consultas simples, temos a possibilidade de usar operadores lógicos:

```mongodb
db.nome_colecao.find({"campo.subcampo":"Valor"})
// Exemplo
db.usuarios.find({"endereco.cidade": "São Paulo"})
```

Temos os seguinte **operadores lógicos**:

* $and
* $or
* $not

Exemplos:

1) AND

```mongodb
{idade: 20, nome: "Carlos"}
{$and: [ {idade:20}, {nome: "Carlos"} ]}
```

2) OR
```mongodb
{$or: [ {idade: 20}, {nome:"Carlos"} ]}
```

E temos os seguintes **operadores de comparação**:

* $eq: Igualdade
* $ne: Diferente
* $gt: Maior que
* $gte: Maior igual que
* $lt: Menor que
* $lte: Menor igual que
* $in: Está em
* $nin: Não está em

Exemplo:
```mongodb
{$and: [{idade: {$ne: 20}}]} \\Retorna todos que a idade é diferente de 20.
{idade: {$gte: 30}} \\Retorna todas que tem idade >= 30.
{cidade: {$in: ["São Paulo", "Belo Horizonte"]}} \\Retorna todos os registros que tem como cidade SP ou BH
```



### Projeções

Chama-se projeção quando define-se quais campos devem ser retornados em uma consulta.

### Ordenação

Conhecida como **sort** dentro do MongoDB. Ordena os resultaos de uma consulta com base em um ou mais campos.

### Limitação

Pode-se limitar o número de documentos retornados em uma consulta.

### Paginação

É a estratégia de retornar dados por demanda, para não ter que retornar todos os dados de uma vez. Pode ser feito:

```mongodb
db.nome_colecao.find().skip(10).limit(5)
```
* **skip(n)**: Quantos registros vai ignorar
* **limit(m)**: Quantos registros vai retornar após o skip

### Atualizando Documentos

```mongodb
db.nome_colecao.updateOne()
db.nome_colecao.updateMany()
db.nome_colecao.replaceOne()
```

Alguns operadores de **update**:

* $inc : Incrementa
* $push: Adiciona informação, não precisa estar em forma de array.
* $set: Atribui a uma determinada chave um determinado valor,
* $unset
* $rename

Por exemplo, vamos supor que na nossa coleção "nome_coleção" tenha o a chave "nome" e que um valor seja "Thiago", "nome": "Thiago". Podemos alterar para "Thiago William:

```mongodb
db.nome_colecao.findOneAndUpdate({"nome":"Thiago"}, {$set: {"nome": "Thiago William"}})
```

Mas imagina que na nossa coleção, tivessemos 'n' documentos com nome Thiago, poderiamos atualizar a idade de todos de uma vez, fazendo:

```mongodb
db.nome_colecao.updateMany({"nome":"Thiago"}, {$set: {"idade": 31}})
```

Se usássemos o comando "updateOne()" ele atualizaria apenas 1 documento.  
Agora, imagina que queremos adicionar um campo contador "viagens", e incrementá-lo. Poderíamos fazer da seguinte maneira:

```mongodb
db.nome_colecao.updateMany({"nome":"Thiago"}, {$set: {"viagens": 0}})
db.nome_colecao.updateMany({"nome": "Thiago"},{$inc: {"viagens": 1}})
```

Agora imagina que precisamos adicionar o campo de 'interesses', que será um campo que contém um array com todos os interesses da pessoa:

```mongodb
db.nome_colecao.updateMany({"nome": "Thiago"}, {$set: {"interesses": ["culinaria"]}})
```
Para atualizar os interesses, ou seja, inserir mais interesses usamos o **$push**:

```mongodb
db.nome_colecao.updateMany({"nome": "Thiago"}, {$push: {"interesses": "skateboard"}})
```


[Operadores de Update](https://www.mongodb.com/docs/manual/reference/operator/update/)

### Excluindo Documentos

```mongodb
db.nome_colecao.deleteOne({});
db.nome_colecao.deleteMany({});
```

Por exemplo, vamos excluir o valor "Thiago" da chave "nome":

```mongodb
db.nome_colecao.findOneAndDelete({"nome":"Thiago"})
```

Poderia excluir da outra maneira:

```mongodb
db.nome_colecao.deleteOne({"nome":"Thiago"})
```

E se tivessemos diversos Thiagos, poderíamos excluir todos:

```mongodb
db.nome_colecao.deleteMany({"nome":"Thiago"})
```

## Introdução ao Redis

É um banco de dados NoSQL muito potente e utilizado. É um sistema de armazenamento de dados em memória de alto desempenho. Ele oferece uma estrutura muito versátil e é amplamente utilizado para armazenar gerenciar e manipular dados em Cache, no geral, não é utilizado como BD principal, mas pode ser. Lembrando que ele armazena dados em memória e, portanto, com um restart do servidor a informação é perdida. Suas principais características são:

* Armazenamento em memória,
* Estrutura de dados versátil,
* Operações atômicas,
* Cache de alto desempenho,
* Pub/Sub (Publicação/Assinatura)

Ele é do tipo **chave:valor**, mas não se deve confundi-lo com tipo documentos, o tipo documento é composto de diversas chaves e valores, mas o Redis armazena apenas chaves:valores sem relação nenhuma uma com a outra. Suas principais utilizações são:

* Cache de dados,
* Filas de mensagens,
* Contagem de acessos e estatísticas em tempo real,
* Gerenciamento de sessões,
* Cache de resultados de consultas.

Os principais comandos do Redis são:

* SET: Adicionar informação,
* GET: Trazer a informação
* DEL: Excluir a informação
* EXISTS: Verificar se já existe uma chave,
* KEYS: Trazer as chaves,
* INCR: Incrementar variável numérica,
* DECR: Decrementar variável numérica.
* EXPIRE: Define um tempo de vida de um dado,
* TTL: Retorna o tempo de vida de um dado,
* LPUSH: Insere diversos valores em uma chave,
* LRANGE: Retorna os valores da chave. O comando necessita: LRANGE chave inicio fim (Ex: LRANGE usuarios 0 -1)

O Redis só permite busca por **chave**, não é possível fazer busca por valor.


[Teste o Redis](https://try.redis.io/)

