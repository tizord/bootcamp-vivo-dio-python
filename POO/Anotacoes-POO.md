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