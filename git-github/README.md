## Curso de Git/Github

### Instalando no Ubuntu

1) Adicionar PPA para instalar a versão mais estável do Git

```console
sudo add-apt-repository pp:git-core/ppa
```

2) Atualizar o OS para a versão mais nova e estável

```console
sudo apt-get update git
```

3) Instalando o Git

```console
sudo apt install git
```
4) Verificando a versão do git
```console
git --version
```

### Configurando o Git

O comando git config traz todas as opções de configurações. Entre as configurações temos algumas opções, entre elas:  
* --global: Referente ao usuário,  
* --system: Referente ao sistema (e todos os usuários),
* --local: Referente ao repositório

Agora, vamos configurar o nome do usuário e o email:  

```console
git config --global user.name "Nome"
git config --global user.email "email@email.com"
```

Para achar o nome da branch padrão e para trocar o nome são os comandos, respectivamente:

```console
git config init.defaultBranch
git config --global init.defaultBranch nome
```

Para trazer todas as configurações globais/sistemas/locais:

```console
git config --global --list
```
Onde altera-se o --global por --system ou --local

### Autenticando a conta do Github

#### Via token

No **github**:

setting > developer setting > personal access token > tokens (classic) > generate new token (claasic)  
Um token vai ser gerado, deve ser copiado e colado no campo "senha", no Bash.  
O token pode ter validade e para não ter que ficar inserindo o token podemos fazer os seguintes passos:  
Se a máquina for compartilhada e você deseja salvar o token temporariamente:
```console
git config credential.helper cache
```
Se você é o único usuário da máquina e quer salvar  

```console
git config --global credential.helper store
```
Para saber em qual local do computador o Git guardou a credencial usamos:

```console
git config --global --show-origin credential.helper
```

#### Via SSH


Primeiro vamos verificar se já existe chave SSH:  
```console
ls -a ~/.ssh
```
Caso não tenha, temos que criar:  
```console
ssh-keygen -t ed25519 -C "email@email.com"
```
Isso irá gerar uma chave SSH privada e, então temos que adicioná-la ao ssh-agent:

```console
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat id_ed25519.pub
```
Deve-se copiar o resultado do último comando e:
Acessa o **github**:  
setting > SSH and GPG keys > New SSH key  
Colar a chave no campo "key"

### Primeiros Passos

Iniciando um repositorio:
```console
git init
```

Para clonar um repositório (1) ou para clonar um repositorio e alterar seu nome (2) ou então para clonar uma branch de um determinado repositório (3) faz-se, respectivamente:
```console
git clone URL
git clone URL novo_nome
git clone URL --branch nome_branch --single-branch
```
Para clonar uma determinada

Para se conectar ao repositório remoto:  
```console
git remote add nome_repositorio_remoto URL 
```
O comando git status traz o status do repositório: sem tem alterações, se está vazio, se está atualizado...  
```console
git status
```