# Introdução ao desenvolvimento Web

Desenvolvimento web refere-se ao processo de criação de websites e aplicações para a internet ou uma intranet. Abrange uma varidade de tarefas como:
* Web Design,
* Programação Web,
* Gestão de Bando de Dados,
* Engenharia de Servidores.

### Componentes Principais

* Frontend: É a parte do Website que os usuários interagem diretamente. Envolve a criação de itnerfaces de usuários e experiências, usando tecnologias como HTML, CSS e JavaScript,
* Bakcend: É a parte onde ocorrem processamento de dados, gerencimaneto de banco de dados e controle de servidor. Envole linguagens como Python, Java

## Como A Web Funciona

A internet é uma rede global de computadores interconectados. A Web é um sistema de informação construído sobre a internet que utiliza o protocolo HTTP para transmitir dados. Dentro da rede interconectada pública (internet), podemos rodar várias aplicações, como FTP, E-mail, Telnet. Isso pode ser visto, pelo e-mail, onde instalamos um cliente de e-mail (outlook, thunderbird), configuramos esse cliente para um servidor SMTP, ou seja, um servidor que roda a aplicação de e-mails, e enviamos/recebemos e-mail por esse cliente, sem acessar a web.


### Protocolo HTTP

O HTTP é o protocolo fundamental usado na Web para a transferência de dados. Quando um usuário acesa um site, o navegador envia uma solicitação HTTP para o servidor do site, que responde com os dados do site.

**Funcionamento de um Website**

1) **Solicitação do usuário**: Usuário insere uma URL no navegador ou clica em um link,
2) **Resolução de DNS**: O URL é traduzido em um **endereço IP** através do sistema **DNS**,
3) **Conexão com o servidor**: O navegador utiliza o endereço IP para estabelecer uma conexão com o servidor que hospeda o site,
4) **Resposta do servidor**: O servidor processa a solicitação HTTP e envia de volta os arquivos (HTML, CSS e JS),
5) **Renderização no navegador**: O navegador interpreta esses arquivos e exibe o site ao usuário.


## API

API (Interface de Programação de Aplicações) é um conjunto de regras e definições que permite que diferentes aplicações de software ou componentes se comuniquem entre si. Funciona como um intermediário, permitindo que pedidos sejam feitos e respotas sejam recebidas entre diferentes sistemas de softwares.

As APIs são cruciais para a construção de aplicações modernas e escaláveis. Elas permitem a flexibilidade para integrar e expandir funcionalidades sem reinventar a roda.


## Tipos de API

### API RESTful

RESTful refere-se a APIs que seguem os princípios do REST (Representational State Transfer). São baseadas em HTTP e utilizadas para interações Web. Envia em formato JSON e recebe em JSON.

**Características**

* Uso dos métodos HTTP (GET, POST, PUT, DELETE) para operações CRUD,
* Curva de aprendizado menor,
* Fácil de entender e implementar

### API SOAP

SOAP (Simple Object Access Protocol) é um protocolo que define um padrão para a troca de mensagens baseadas em XML. O conteúdo [SOAP da W3 Schools](https://www.w3schools.com/xml/xml_soap.asp) explica bem o SOAP.

**Características**

* Protocolo baseado em XML para troca de informações,
* Independente de linguagem e plataforma de transporte,
* Suporte para operações complexas e segurança avançada

### API GraphQL

Uma linguagem de consulta para sua API, e um servidor capaz de executar essas consultas, retornando apenas os dados especificados.

**Características**

* Permite que os clientes especifiquem exatamente quais dados querem,
* Eficiente na redução de solicitações e no tamanho dos dados transferidos,
* Flexível e fortemente tipada, facilitando a evolução das APIs


## Verbos HTTP

Em APIs RESTful, os verbos HTTP têm papeis específicos que se alinham com as operações CRUD. Esta abordagem padronizada permite que as APIs sejam intuitivas e previsíveis, facilitando a interação entre diferentes sistemas e aplicações. Dessa forma, temos as **convenções RESTful**:

* **GET**: Leitura,
* **POST**: Criação,
* **PUT/PATCH**: Atualização,
* **DELETE**: Remoção.


# FastAPI

Framework de alta permonfance, fácil de aprender, fácil de codar, pronto para produção.