## Introdução a POO

POO (**Programação Orientade a Objetos**) é um paradigma de programação, ou seja, uma forma de
estruturar os programas. A ideia é abstrair problemas em objetos do mundo real, onde os dois elementos chaves são: **classe** e **objeto**.  
**Classe**: Define as características e comportamentos de um objeto, mas não pode ser usada por si só.  
**Objeto**: É uma instância da classe, ou seja, um objeto dessa classe.  
 Veja um exemplo em Python:  
 **Clase**  
 Abaixo teremos a classe Cachorro. Na classe cachoro temos o CONSTRUTOR, que recebe self (que é o proprio objeto).
 Temos 2 métodos: latir e dormir.  
```python
 class Cachorro:
    
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(self):
        print("Au Au Au")
    
    def dormir(self):
        self.acordado = False
        print("ZZzzZZzz...)
```

**Objeto**  
Agora podemos criar os objetos da classe cachorro, ou seja, instâncias da classe ou cachorros conhecidos.  
```python
cachorro1 = Cachorro("Mafalda", "Branco")
cachorro2 = Cachorro("Thunder", "Marrom")

cachorro1.latir()
cachorro2.dormir()
```

**Contrutores** e **Destrutores**  

**Contrutor**  
O Contrutor em Python é dado pelo método __init__, ele sempre é executado para inicializar uma instância da classe.
Serve para inicializar valores e dar o estado inicial de um objeto.  

**Destrutor**  
O destrutor em Python é dado pelo método __del__, e ele é usado quando uma instância é destruída. Em Python eles não são tão necessários quanto em C++ porque o Python tem um coletor de Lixo com lida com o gerenciamento de memória.  
```python
def __del__(self):
    ação
```
E por fim, seria chamado assim:

```Python
c = Cachorro(parametros)
del c
```
## Herança

É a capacidade de uma classe filha herdar características e comportamentos da classe pai.
Possui o benefício da reutilização do código e é de natureza transitiva onde, se a classe B herdar da classe A, todas as subclasses de B também vão herdar de A.
É importante lembrar da relação **Herança x Polimorfismo**

```Python
class A:
    pass
class B(A):
    pass
```

### Herança Simples
Herda apenas de uma classe pai

### Herança Múltipla
Herda de múltiplas classes pai. Existe o problema de ter dependência de forma cíclica, algumas linguagens não implementam esse tipo de herança.

Temos o método 
```Python
classe.__mro__
Ou
print(Classe.mro())
```
Que irá trazer a ordem de resolução das Classes.

## Encapsulamento

É um dos conceitos fundamentais em POO, descreve a ideia de agrupar dados, atributos e métodos em uma unidade, impondo restrições de acesso afim de evitar alterações acidentais.
Em Python não temos palavras reservas porém usamos convenção no nome do recruso para definir se um método/atributo é publico ou privado:  
Publico: Acessível fora da classe,  
Privado: Acessível apenas dentro da classe.  

```Python
class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self._idade = idade
    
```

Apesar disso, o Python deixa acessar e manipular o recurso, mas por convenção não se deve mexer. Para isso, deve-se ter métodos para manipular os atributos privados. Em Java temos os métodos **getters** e **setters**

Podemos usar o **property()** que permite criar atributos gerenciados (conhecidos como propredades) quando necessitar modificar sua implementação interna sem alterar a API pública da classe. Olha como podemos usar:

```Python
class Foo:
    def __init__(self, x=None)
    self._x = x

    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, value):
        _x = self._x or 0
        _value = value or 0
        self._x = _x + _value
    
    @x.deleter
    def x(self):
        self._x = -1

foo = Foo(10) #1
foo.x = 10    #2
del foo.x     #3
```

No exemplo acima, na linha #1 criamos o objeto foo com valor de 10. Após, passamos o valor 10 para a atributo x, porém repare que o atributo da classe Foo é _x e por isso essa atribuição não é possível.
A classe Foo tem um "método" x que faria essa adição, e quando usamos o @property, mudamos sua forma de atuação e ele passa a atuar como um atributo em vez de atuar como método. O valor 10 ira para o property, que irá para o @x.setter que fará a adição e poderemos alterar o atributo _x sem alterá-la diretamente. Nesse momento é importante perceber que estamos modificando um método em atributo e por isso devemos mnipular como um atributo.

## Interfaces e Classes Abstratas

### Variáveis de classe, variáveis de instância, métodos de classe e métodos de instância

**Atributo de classe:** É compartilhado pelos objetos da classe,  
**Atributo de instância:** São diferentes para cada objeto.  
Métodos de classe: Estão ligados à classe e não ao objeto, eles têm acesso ao estado da classe, são utilizados para criar **métodos de fábrica**  
**Método estático:** Não recebe um primeiro argumento explícito, é um método vinculado à classe e não ao objeto da classe, ele não pode acessar ou modificar o estado da classe. São utilizados para criar **funções utilitárias**, ou seja, são funções que não dependem da classe necessariamente. Exemplo:  

Vamos avaliar dois cenários:
1) A classe Pessoa que contém um método para criar um objeto a partir da data de nascimento, que recebe um objeto pessoa e terá que instânciar outro objeto pessoa, o que não é ideal.

Repare que no construtor de pessoa, temos que passar nome e idade = None, caso contrário o método não iria funcionar uma vez que o construtor pede 2 argumentos.


```Python
class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    def criar_de_data_nascimento(self, ano, mes, dia, nome):
        idade = 2024 - ano
        return Pessoa(nome, idade)
    
p = Pessoa("Thiago", 31)
print(p.nome, p.idade)

p = Pessoa().criar_de_data_nascimento(1993, 9, 11, "Thiago")
print(p.nome, p.idade)


```

Dessa forma, é ideal transformar o método "criar_de_data_nascimento" em um método de classe. isso é feito usando o decorador @classmethod
Por convenção, quando usamos o @classmethod, não usamos a palavra "self" e sim "cls".

Isso significa que, como o método virou um método de classe, invocamos ele de forma diferente:

p = Classe.método_de_classe()

Por fim, criamos um método estático usando o decorador @staticmethod

```Python

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

p = Pessoa("Thiago", 31) #Thiago 31
print(p.nome, p.idade)

p = Pessoa.criar_de_data_nascimento(1993, 9, 11, "Thiago")
print(p.nome, p.idade) #Thiago 31

print(Pessoa.e_maior_idade(17)) #False
print(Pessoa.e_maior_idade(27)) #True
```
Repare que o método estático "e_maior_idade" independe de alguma instância desse objeto.

### Interfaces

Interfaces definem o que uma classe **deve** fazer e não **como** fazer. Em outras palavras a interface serve para definir um contrato, onde são declados os métodos e suas respectivas assinaturas. Em Python utilizamos **classses abstratas** para criar contratos, essas classes **não podem** ser instanciadas.  


### Classes Abstratas

Por padrão o Python não fornece classes abstratas e por isso é necessário usar o módulo abc. O abc funciona decorando métodos da classe base como abstratos e, em seguida, registrando classes concretas como implmentações da base abstrata. O método se torna abstrato quando usamos o decorador @abstractmethod

Então, de forma concisa, a classe abstrata obriga o desenvolvedor a implementar seus métodos em cada uma das classes que herdam dela.  
Para usar a classe abstrata é necessário importar o módulo ABC. Vamos criar uma classe abstrata ControleRemoto que terá os métodos ligar e desligar. Após vamos criar a classe ControleTV que herda de controle remoto:

```Python

from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class ControleTV(ControleRemoto)
    pass

```

Dessa forma não será possível instanciar o ControleTV, será apresentado o erro dizendo que é obrigatório implementar os métodos.
Logo temos que fazer:

```Python

from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class ControleTV(ControleRemoto)
    def ligar(self):
        print("Ligando TV...")
        print("TV ligada")
    
    def desligar(self):
        print("Desligando TV...")
        print("Tv desligada")

controle = ControleTV()
controle.ligar()
controle.desligar()

```

Podemos criar também propriedades abstratas:

```Python

from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto)
    def ligar(self):
        print("Ligando TV...")
        print("TV ligada")
    
    def desligar(self):
        print("Desligando TV...")
        print("Tv desligada")
    
    @property
    def marca(self):
        return "Marca1"

controle = ControleTV()
controle.ligar()
controle.desligar()

```

Dessa forma, teremos nossa classe funcionando.


## Decoradores

Antes de estudarmos decoradores, temos que: **funções** em Python são objetos de primeira classe, ou seja, **elas podem ser passadas e usadas como argumentos**.


Além disso, temos o conceito de **inner functions**, ou seja, funções definidas dentro de outra função, o Python permite "cascatear" função dentro de funções. É possível retornar funções também.

Vamos olhar mais de perto um caso. No código exibido abaixo vamos explorar as funções passadas como parâmetros. Vamos olhar algumas formas:



```python


def mensagem(nome: str):
    print('Executando nome')
    return f'Oi {nome}'

def mensagem_longa(nome:str):
    print('Executando mensagem longa')
    return f'Oi {nome}, tudo bem com você?'

def executar(funcao):
    print('Executando executar')
    return funcao()

executar()
```

Repare que no exemplo acima, o código irá resultar em um **erro**, pois executar() necessita um argumento e nenhum argumento foi passado. Sendo assim, vamos passar um argumento:

```python

executar(mensagem('João'))

```

O código acima possui para a função *executar*, mas ainda assim irá resultar em um **erro**, dizendo que o tipo *'str'* não é um callable, ou seja, não podemos passar o 'João' pois, dessa forma, é como se estivessemos executando a função *mensagem* dentro do parâmetro da função *executar* quando na verdade deveriamos apenas passar a função *mensagem* como parâmetro. Sendo assim, vamos passar a função *mensagem* apenas como referência:


```python
executar(mensagem)

```

Mais uma vez o código irá apresentar um problema, pois *mensagem()* necessita um argumento posicional (nome). Hora, como podemos resolver isso? Dessa forma, temos duas opções para resolver:

```python


def mensagem(nome: str):
    print('Executando nome')
    return f'Oi {nome}'

def mensagem_longa(nome:str):
    print('Executando mensagem longa')
    return f'Oi {nome}, tudo bem com você?'

def executar(funcao, nome: str):
    print('Executando executar')
    return funcao(nome)

executar(mensagem, "João") # Mais ainda assim não irá retornar o nome, a saída será:
>> executando executar
>> executando mensagem

# Para mostrar o nome é necessário que:

print(executar(mensagem, "João"))
>> executando executar
>> executando mensagem
>> Oi João

```
Acima temos o exemplo referente a passar funções como parâmetros. Agora vamos olhar para as funções internas:

```Python
def principal():
    print('Executando a função principal')

    def funcao_interna():
        print('Executando a função interna')
    
    def função_2():
        print('Executando a função 2')
    
    função_interna()
    função_2()

principal()

```

No exemplo acima teremos a seguinte saída:

```Python
>> Executando a função principal
>> Executando a função interna
>> Executando a função 2
```

Por fim, podemos usar funções como retorna, veja o exemplo:

```Python

def calculadora(operacao: str):
    def soma(a, b):
        return a + b
    
    def sub(a, b):
        return a - b
    
    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b
    
    match opercao:
        case "+":
            return soma
        
        case "-":
            return sub
        
        case "*":
            return mul
        
        case "/":
            return div

#1
print(calculadora('+'))
>> <function calculadora.<locals>.soma at ....>
#2
print(calculadora('+')(2,2))
>> 4
#3
op = calculadora('+')
print(op(2,2))
>> 4

```
Acima, podemos ver que é possível retornarmos a referência para a função como no exemplo **#1**.

Agora que vimos que funções são como qualquer outro objeto em Python, podemos ver a mágica que é o **decorador Python**. Veja um exemplo de um **decorador simples**

### Decorador Simples

```Python
def meu_decorador(funcao):
    def envelope():
        print('Faz algo antes de executar a função')
        funcao()
        print('Faz algo depois de executar a função')

    return envelope

def ola_mundo():
    print('Olá mundo!')

#1
ola_mundo()
>> Olá mundo!
#2
ola_mundo = meu_decorador(ola_mundo)
>> Faz algo antes de executar a função
>> Olá mundo!
>> Faz algo depois de executar a função

```

O decorador serve para, por exemplo, fazer uma checagem de segurança antes de executar a função. Os decorados servem para colocar mais comportamento dentro de uma outra função. Os decoradores são um **pattern**.

**Acúçar sintático: @**

O Python permite que você use decoradores de maneira mais simples com o símbolo **@**:

```Python
def meu_decorador(funcao):
    def envelope():
        print('Faz algo antes de executar a função')
        funcao()
        print('Faz algo depois de executar a função')

    return envelope

@meu_decorador
def ola_mundo():
    print('Olá mundo!')

ola_mundo()
>> Faz algo antes de executar a função
>> Olá mundo!
>> Faz algo depois de executar a função
```

### Funções de Decoração com Argumentos

Podemos usar *args e **kwargs na função interna, com isso ela aceitará um número arbitrário de argumentos posicionais e de palavras-chaves.

```Python
def duplicar(funcao):
    def envelope(*args, **kwargs):
        print('Faz algo antes de executar a função')
        funcao(*args, **kwargs)
        funcao(*args, **kwargs)
        print('Faz algo depois de executar a função')

    return envelope

@duplicar
def aprender(tecnologia):
    print(f'Estou aprendendo {tecnologia}')

aprender("Python")
>> Faz algo antes de executar a função
>> Estou aprendendo Python
>> Estou aprendendo Python
>> Faz algo depois de executar a função
```

### Retornando valores de funções decoradas

O decorador pode decidir se retorna o valor da função decorada ou não. para que o valor seja retornado a função de **envelope** deve retornar o valor da função decorada.

```python
def duplicar(funcao):
    def envolope(*args, **kwargs):
        funcao(*args, **kwargs)
        return funcao(*args, **kwargs)
    
    return envolope

@duplicar
def aprender(tecnologia):
    print(f'Estou aprendendo {tecnologia}')
    return tecnologia.upper()

tecnologia = aprender("Python")
```
### Introspecção

A introspecção é a capacidade de um objeto saber sobre seus próprios atributos em tempo de execução. Como assim? Vamos reparar no seguinte código:

```python
print.__name__
>> 'print'
```
Se fizermos isso com o nosso código *aprender*:

```python
aprender.__name__
>>'envelope'
aprender
>> <function duplicar.<locals>.envelope at 0x7....>
```

Ou seja, a nossa capacidade de introspecção está comprometida, pois não estamos colocando o nome correto da função *aprender*. Para corrigir isso, temos que fazer:

```python

def duplicar(funcao):
    @functools.wraps(func)
    def envolope(*args, **kwargs):
        funcao(*args, **kwargs)
        return funcao(*args, **kwargs)
    
    return envolope

@duplicar
def aprender(tecnologia):
    print(f'Estou aprendendo {tecnologia}')
    return tecnologia.upper()

tecnologia = aprender("Python")
print(tecnologia)
```
O módulo *functools* e seu método *wraps*, mantém o nome da função e os parâmetros da função passada como argumento, para que não se perca a capacidade de introspecção.

## Iteradores e Geradores

Esses dois conceitos nos permite trabalhar com sequência de maneira poderosa, quando se tem objetos iteráveis, se ele for muito grande, pode-se ter problemas como demora de execução, de uso intensivo de memória e acabar tendo Overflow. Portanto, esses dois mecanismos (**iteradores e geradores**) servem para resolver esse problema.

### Iteradores

Um iterador é um objeto que contém um número contável de valores que podem ser iterados, ou seja, pode-se percorrer todos os valores. O protocolo do iterador é uma maneira do Python fazer a iteração de um objeto, que consiste em dois métodos especiais:  
* **__iter__()**
* **__next__()**

Ou seja, se criarmos uma classe e adicionarmos esses dois métodos, a nossa classe passa a ter objetos iteráveis. Vamos ver um exemplo de um iterador que recebe uma lista e devolve o dobro de cada valor:

```python
class MeuIterador():
    def __init__(self, numeros:list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration

for i in MeuIterador():
    print(i)

```
Aqui vamos explicar alguns pontos:

1) É obrigatório que o método __iter__ retorne algo, pois, caso não seja definido um retorno, ele retornará (por padrão do Python) *None* e *None* não é iterável, o que faria nosso programa dar erro.
2) É obrigatório que o método __next__ tenha o **raise StopIteration** pois é isso que permite o reconhecimento do fim da iteração. Caso não seja passado o **raise**, a classe entrará em loop infinito.
3) Usamos o try/except pois o Python vai reconher que o contador vai ter uma valor maior do que o tamanho da lista e vai lançar o erro de Index, que é justamento nossa condição de parada.


### Geradores

São tipos especiais de iteradores, ao contrário das listas ou outros iteráveis, não armazenam todos os valores na memória.  
São definidos usando funções regulares, mas, em vez de retornar valores usando **return** usam **yield**.
Mas qual a diferença?

A principal caracteristica de um gerador é que ele economiza de maneira otimizada a memória da sua máquina. Imagina que vocẽ tenha uma lista com 100 clientes onde os 100 clientes são retornados por um método. Por debaixo dos panos o interpretador Python deve alocar uma região de memória para guardar essa lista com os 100 usuários. Quando usamos o gerador, o Python não precisa alocar essa memória para todos os 100 usuários, pois não é necessário retornar todos os 100 de uma única vez, o gerador permite retornar os usuários de um em um. Vejamos as características de um gerador:  

* Uma vez que um item é consumido ele é esquecido e não pode ser acessado novamente,
* O estado interno de um gerador é mantido entre chamadas,
* A execução de um gerador é pausada na declaração **yield** e retomada daí na próxima vez que ele for chamado

Repare na criação de um gerador:

```python

def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

for i in meu_gerador(numeros = [1, 2, 3]):
    print(i)

```

O código acima é suficiente para a criação de um gerador.

Vamos criar um método de recuperar dados de uma API usando um gerador. Para isso teremos que:
* Solicitar dados por páginas (paginação),
* Fornecer um produto por vez entre as chamadas,
* Quando todos os produtos de uma página forem retornados, verificar se existem novas páginas,
* Tratar o consumo da API como uma lista Python

```python
import requests

def fetch_products(api_url, max_pages=100):
    page = 1
    while page <= max_pages:
        response = requests.get(f'{api_url}?page={page}')
        data = response.json()
        for product in data['products']:
            yield product
        if 'next_page' not in data:
            break
        page += 1

# Uso do gerador
for product in fetch_products("http://api.example.com/products'):
    print(product['name'])

```
