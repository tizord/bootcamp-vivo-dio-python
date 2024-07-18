# Data, Hora e Fuso

## Introdução

O módulo **datetime** é usado para lidar com datas e horas.

```python
import datetime

d = datetime.date(2024,7,3)
print(d)
>>> 2023-07-03
```

O módulo **datetime** está na documentação oficial do Python:  
[Python - Datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)

Temos o objeto *datetime*, que é um único objeto contendo todas as informações de um objeto *date* e um objeto *time*.

```python
import datetime
datetime.datetime(year, month, day, hour, minuto, second, microsecond, tzinfo, *, fold)

data_hora= datetime.datetime(2024, 7, 3, 22, 8)
print(data_hora)
>>> 2024-07-03 22:08:00
```

Temos o método **today()**, que traz a data, hora minutos e segundos do local.

Por fim, podemos ver, também, o méotodo *time()* que traz as informações de hora:

```python
from datetime import time

hora = time(10,20, 0)
print(hora)
>>> 10:20:00
```
## Manipulação de Datas e Horas

Podemos criar e manipular objetos date, time e datetime de várias maneiras, podemos adicionar e subtrair datas, verificar a diferença entre datas etc. Essas manipulações são feitas usando a classe *timedelta*

```python
import datetime

d = datetime.datetime(2024, 7, 3, 22, 15)
print(d)
>>> 2024-07-03 22:15:00
d = d + datetime.timedelta(weeks=1)
print(d)
>>> 2024-07-10 22:15:00
```
Repare que o objeto timedelta representa a duração, a diferença entre duas datas ou horas. No geral, as operações mais comuns são: **adição** ou **subtração** de timedeltas.

Para usar o timedelta, fazemos:

```python

from datetime import datetime, timedelta

data_atual = datetime.now()
tempo_processo = 45
data_estimada = data_atual + timedelta(minutes=tempo_processo)
print(data_estimada)
```

No timedelta, temos que indicar qual unidade de tempo estamos falando (minutos, horas, etc).

Mas repare que não é possível realizar uma operação do tipo **time - timedelta**, pois o timedelta necessita um objeto que tenha o date junto. Para realizar essa operação é necessário, passar um datetime, realizar a operação em horas e extrair só a parte de horas com o time:

```python
resultado = datetime(2024, 7, 4, 18, 12, 00) - timedelta(hours=1)
resultado.time()
```

### Conversão e Formatação de Datas e Horas

Para fazer a conversão de datas e horas usamos:  
* strftime (string format time)
* strptime (string parse time): Converte string em datetime

Por exemplo:

```python
import datetime

d = datetime.datetime.now()

# Formatando hora e data
print(d.strftime("%d/%m/%Y %H:%M"))
>>> 04/07/2024 18:25

# Convertendo string para datetime
string_data = "04/07/2024 18:26"
d = datetime.datetime.strptime(string_data, "%d/%m/%Y %H:%M")
print(d)
>>> 2024-07-04 18:26:00
```
O **strftime** pode cortar partes do objeto **datetime**, ou seja, podemos exibir apenas o dia/mes, ou dia/mes/ano, ou só as horas. Na documentação, temos todas as opções de máscara, mas podemos ver mais um exemplo:

```python
data_hora_atual = datetime.now()
data_hora_str = "2024-07-04 18:36"
mascara_ptbt = "%d/%m/%Y %a"
print(data_hora_atual.strftime(mascara_ptbt))
>>> 04/07/2024 Thu
```

### Timezone

É possível trabalhar com fuso-horário através do módulo **pytz**:

```console
pip install pytz
```

```python

import datetime
import pytz

d = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
print(d)
>>> 2024-07-06 13:29:51.051327-03:00

```

O módulo **datetime** tem o método *utcnow()* que traz o fuso referência. É sempre recomendado salvar as datas/horas em UTC e fazer a conversão dentro do código. A biblioteca **datetime** também oferece suporte a fuso-horário, porém de maneira mais verbosa.


# Arquivos

Um arquivo é um container no computador onde as informações são armazenadas em formato digital. Em Python podem manipular dois tipos de arquivos:  
* Arquivos de Texto
* Arquivos Binários

## Abrir e Fechar Arquivos

Para que possamos manipular arquivos em Python, primeiro é necessário abri-los. Para abrir os arquivos usamos a função **open()** e, para fechar usamos a função **close()**.

```python

file = open("arquivo.txt", "r")
file.close()
```

Existem alguns modos de para abrir um arquivo, que é passado como segundo argumento:

1) r: read (somente leitura),
2) w: writing (Para gravação, o conteúdo anterior é apagado),
3) a: appending (anexar),
4) x: Exclusive creation (Só funciona se o arquivo não existir, daí ele cria o arquivo),
5) b: Binary (Binário)
6) t: Text (Modo texto, padrão)
7) +: Update (leitura e escrita)

### Lendo arquivos

Para ler um arquivo, devemos usar o método **read(), readline(), readlines()**. A diferença é que:
* read(): Lê o arquivo todo de uma vez. Coloca tudo em uma string.
* readline(): Lê uma linha por vez,
* readlines(): Retorna uma lista onde cada elemento é uma linha do arquivo

Imagina o seguinte arquivo:

"Linha1,
 ...
 Linha n "

```python

file = open("arquivo.txt", "r")
print(file.read())
>>> "Linha1, ..., Linha n"

print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
>>> "Linha1"
>>> "..."
>>> "Linha n"
>>>

print(file.readlines())
>>> ["Linha1", "...", "Linha n"]

file.close()
```

Uma forma de usar o **readline()** é:

```python
while len(linha := arquivo.readline()):
    print(linha)
```
Repare que essa forma é uma forma rápida de trazer linha a linha, para arquivos muito grandes. Outra forma é implementar o iterador.

### Escrevendo em Arquivos

Para escrever em um arquivo usamos a função **write()** ou **writelines()**. Porém, deve-se lembrar de abrir o arquivo no modo correto.


```python
file = open("arquivo.txt", "w")
file.write("Olá, mundo!")
file.close()
```

## Gerenciando Arquivos e Diretórios

O Python oferece funções para gerenciar arquivos e diretórios (criar, renomear e excluir), isso é feito usando os módulos **os** e **shutil**.

```python
import os
import shutil

# Cria um diretório
os.mkdir("Exemplo")

# Renomeia um arquivo
os.rename("Old.txt", "New.txt")

# Remove um arquivo
os.remove("Unwanted.txt")

# Move um arquivo
 shutil.move("source.txt", "destination.txt")
```

Repare que na criação do diretório, temos um problema de onde ele vai criar esse diretório, geralmente na raíz. Para contornar esse problema, ou seja, definir onde ele deve criar o arquivo, podemos usar o módulo **pathlib**

```python
import os
from pathlib import Path

ROOT_PATH = Path(__file__)
# Ele retorna o caminho inteiro do arquivo. Para pegar apenas a pasta:

Caminho = ROOT_PATH.parent

# Por fim, podemos fazer:

os.mkdir(ROOT_PATH / "Exemplo")

# O uso da "/" funciona para todos os OS, pois ele é sobrecarregada pelo OS.

```


## Tratamento de Exceções

Os erros mais comuns quando lidando com arquivos:

* **FileNotFoundError**: Quando o arquivo não pode ser encontrado no diretório especificado,
* **PermissionError**: Quando se tenta abrir um arquivo sem as permissões para leitura ou gravação
* **I/OError**: Quando ocorre um erro geral de E/S, como problemas de permissão, falta de espaço em disco, etc
* **UnicodeDecodeError**: Quando ocorre um erro ao tentar decodificar os dados de um arquivo de texto usando uma codificação inadequada.
* **UnicodeEncodeError**: Quando ocorre um erro ao tentar codificar dados em uma determinada codificação.
* **IsADirectoryError**: Quando é feita uma tentativa de abrir um diretório em vez de um arquivo de texto.


Vamos supor que queiramos abrir um arquivo que não existe:

```python
arquivo = open("meu_arquivo.py")
>>> Traceback (most recent call last):
    File ".../dio-python-vivo/Data-Hora-Arquivos-Pacotes/2_arquivos.py", line 20, in <module>
    arquivo = open("meu_arquivo.py")
    FileNotFoundError: [Errno 2] No such file or directory: 'meu_arquivo.py'

# Realizamos o tratamento de erro:

try:
    arquivo = open("meu_arquivo.py")
except FileNotFoundError as exc:
    print("Arquivo não encontrado")

>>> Arquivo não encontrado

```

Agora vamos ver boas práticas:

### Bloco With

Ao declarar **with** tem-se o gerenciamento de contexto, que permite trabalhar com arquivos de forma segura, garantindo que eles sejam fechados corretamente, mesmo em caso de exceções.

```python
with open('arquivo.txt', 'r') as arquivo:
    # Operações
```

Repare que não é necessário usar o **close()**.

### Verificar se o arquivo foi aberto com sucesso

É recomendado verificar se o arquivo foi aberto corretamente antes de executar operações de leitura ou gravação nele. Isso é feito usando o tratamento para **I/OError**:

```python
try:
    with open('arquivo.txt', 'r') as arquivo:
        #comandos
except IOError as exc:
    print(f'Erro ao abrir o arquivo.\n{exc}')
```

### Usar a codificação correta

Deve-se certificar que está usando a codificação corretar ao ler ou gravar arquivos de texto. O argumento **encoding** da função **open()** permite especificar a codificação:


```python
with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
    # Comandos
```
## Arquivos CSV

Os arquivos CSV são arquivos cujos valores são separados por vírgula. O Python possui ummódulo chamado csv para lidar com esse tipo de arquivo.

```python
import csv

with open('exemplo.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

A escrita é feita de maneira análoga:

```python
import csv

with open('exemplo.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Nome", "idade"])
    writer.writerow(["Ana", 30])
    writer.writerow(["João", 29])
```

### Práticas recomendadas

* Usar o **csv.reader** e **csv.writer** para manipular arquivos csv (evite usar .read() e .write()),
* Faça o tratamento correto de exceções,
* Ao gravar arquivos csv definir o argumento **newline=''** no método open.

# Gerenciamento de Pacotes, Convenções e Boas Práticas

Pacotes são módulos que podem ser instalados e utilizados em programas Python. Permite que se utilize códigos escrito por outras pessoas, economizando tempo e esforço. Para usar um pacote, nós usamos o Pip que é um **gerenciador** de pacotes do Python, ou seja, ele permite instalar, atualizar e remover pacotes facilmente. Ele se comunica com o PyPI (Python Package Index) que é onde a maioria dos pacotes Python são armazenados.

[PyPI](https://pypi.org)

```console
pip install pacote
pip uninstall pacote
pip list
```

## Ambientes Virtuais

Os ambientes virtuais permitem manter as dependências de diferentes projetos. Isso é importante para evitar conflitos entre versões de pacotes. O ambiente virtual é criado da seguinte maneira (Linux)

```console
python3 -m venv nome_ambiente_virtual
```
E após ser criado, deve ser ativado (Linux):
```console
source nome_ambiente_virtual/bin/activate
```
Por fim, desativamos o ambiente virtual da seguinte maneira:
```console
deactivate
```

Por exemplo, quando crio ambientes virtuais, costuma usar o nome ".venv":

```console
python3 -m venv .venv
source .venv/bin/activate
deactivate
```

O seguinte post da Alura é muito informativo e direto ao ponto:

[Alura - Ambiente Virtual](https://www.alura.com.br/artigos/ambientes-virtuais-em-python)

Agora vamos ver os principais comandos do pip

* **pip install nome_pacote**: Instala um pacote chamado nome_pacote
* **pip uninstall nome_pacote**: Desinstala o pacote 'nome_pacote'
* **pip list**: Lista os pacotes instalados
* **pip install --upgrade nome_pacote**: Atualiza um pacote

## pipenv

O pipenv é uma ferramenta de gerenciamento de pacotes que **combina a gestão de dependências com a criação de ambiente virtual** para seus projetos e adiciona/remove pacotes automaticamente do arquivo Pipfile, conforme você instala e desinstala pacotes.
O pipenv deve ser instalado globalmente, e deve ser instalado para cada versão do python que você tiver na máquina.

```console
pip install pipenv
pipenv install numpy
pipenv uninstall numpy
pipenv lock
```
O comando **pipenv lock** gera um arquivo com as versões e dependências instaladas no projeto. Além disso, o pipenv tem o comando **pipenv graph** que funciona igual ao pip list, porém ele mostra quais bibliotecas são aninhadas a outras, em forma de árvore, o que é uma enorme vantagem. Vamos ver um exemplo:

Quando instalamos o django, ele traz duas bibliotecas aninhadas (asgiref e sqlparse). Se usarmos o pip unistall django, ele irá remover apenas o django, deixando as duas bibliotecas. O pipenv, quando usamos **pipenv uninstall django**, ainda que desinstale apenas o django, remove do **pipfile.lock** as duas bibliotecas possibilitando o uso do comando **pipenv clean** que irá remover todas as bibliotecas que não estão no default do **pipfile.lock**, ou seja, as bibliotecas aninhadas.

A documentação do pipenv pode ser vista em:

[Pipenv](https://pipenv.pypa.io/en/latest)

## Poetry

Outra ferramenta de gerenciamento de dependências que permite declarar as bibliotecas de que seu projeto depende e gerencia (instala/atualiza/remove) essas bibliotecas. Ele suporta o empacotamento e a publicação de projetos no PyPI

```console
pip install poetry
poertry new myproject
cd myproject
poetry init
poetry install
poetry add numpy
poetry remove numpy
```

O poetry gera um arquivo .toml. No momento que inicializamos o poetry ele faz uma série de perguntas, tudo via CLI. O comando **poetry install** cria o ambiente virtual e instala as bibliotecas definidas. O poetry, através do **remove** remove todos os pacotes aninhados de uma só vez. A documentação do poetry está disponível em:

[Poetry](https://python-poetry.org/docs/)

# Boas Práticas

PEP 8: É um guia de estilo para codificação em Python, ele inclui convenções sobre nomes de variáveis, uso de espaços em branco, comprimento da linha e muitras outras coisas que ajuadm a  manter o código consistente e legível.

[PEP 8](peps.python.org/pep-0008/)

## As principais recomendações:

* Usar 4 espaços para identação,
* Limitar as linhas a 79 caracteres,
* Usar **snake_case** para nomes de variávies e funções,
* Usar **CamelCase** para classes

Para ajudar a seguir as recomendações da PEP 8, podemos usar ferramentas de estilos como o **flake8**.

```console
pip install flake8
flake8 meu_script.py
```

O flake8 tem como padrão o limite de 79 caracteres para um linha. Atualmente utiliza-se 110 ou 120 linhas. Isso pode ser alterado da seguinte forma:

```console
flake8 --max-line-length=120 meu_script.py
```

O flake8, depois de executado, percorre o script informando os erros, mas tem o inconveniente de ter que, além de rodar o comando, entrar no script e adequar. Mas temos outras opção, o **Black**. O **Black** é uma ferramenta de formatação de código Python que segue a filosofia "formato único"; Ele reformata todo o script em um estilo consistente, simplificando a tarefa de manter o código em conformidade com a PEP 8.

```console
pip install black
black meu_script.py
```

Outra ferramenta é o **isort**, que serve para classificar as importações alfabeticamente e separá-las automaticamente em seções.

```console
pip install isort
isort meu_script.py
```

Todas essas ferramentas, podem ser instaladas diratamente no vscode, através da seção de extensões.