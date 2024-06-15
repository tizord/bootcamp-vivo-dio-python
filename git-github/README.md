## Curso de Git/Github

### Instalando no Ubuntu

1) Adicionar PPA para instalar a versão mais estável do Git

```console
sudo add-apt-repository ppa:git-core/ppa
```

2) Atualizar o OS para a versão mais nova e estável

```console
sudo apt-get update
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

O comando git config traz todas as opções de configurações. Entre as configurações temos algumas opções, onde algumas são:  
* --global: Referente ao usuário (do computador),  
* --system: Referente ao sistema (e todos os usuários),
* --local: Referente ao repositório

Agora, vamos configurar o nome do usuário e o email:  

```console
git config --global user.name "Nome"
git config --global user.email "email@email.com"
```

Para achar o nome da branch padrão e para trocar o nome usa-se os comandos abaixo, respectivamente:

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

setting > developer setting > personal access token > tokens (classic) > generate new token (classic)  

Um token vai ser gerado, deve ser copiado e colado no campo "senha", no Bash.  
O token pode ter validade e para não ter que ficar inserindo o token sempre podemos fazer os seguintes passos:  
1) Se a máquina for compartilhada e você deseja salvar o token temporariamente:
```console
git config credential.helper cache
```
2) Se você é o único usuário da máquina e quer salvar  

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
Deve-se copiar o resultado do último comando e, após, acessar o **github**:  
setting > SSH and GPG keys > New SSH key  
Colar a chave no campo "key"

### Primeiros Passos

Iniciando um repositorio:
```console
git init
```

Para clonar um repositório (1) ou para clonar um repositorio e alterar seu nome (2) ou então para clonar uma branch de um determinado repositório (3) faz-se, respectivamente:
```console
(1) git clone URL
(2) git clone URL novo_nome
(3) git clone URL --branch nome_branch --single-branch
```

Para se conectar ao repositório remoto:  
```console
git remote add nome_repositorio_remoto URL 
```
O comando git status traz o status do repositório: se tem alterações, se está vazio, se está atualizado...  
```console
git status
```

Para salvar as alterações no seu repositório, fazemos:
1. Adicionamos os arquivos na fila que será enviada para o Github. Podemos adicionar um arquivo (1) ou todos os arquivos alterados (1.1).
2. Fazemos o commit e adicionamos a mensagem referente a alteração
3. Subimos os arquivos no repositório
4. Opcional: Temos o comando git log que traz informações sobre o commit a ser feito.

```console
1) git add arquivos 
1.1) git add .
2) git commit -m "mensagem"
3) git push -u origin main
4) git log
```

O arquivo **.gitignore** é onde devemos adicionar o nome dos arquivos e pastas que queremos que o git ignore na hora de checar e subir as alterações.  
Os arquivos **.gitkeep** serve para o git reconhecer um diretório vazio. Deve-se colocar esse arquivo dentre do diretório vazio.  

Para restorar um arquivo ao último estado que ele estava, localmente, usamos o comando **git restore**


```console
git restore nome_arquivo
```
Para consertar ou alterar uma mensagem de commit fazemos:


```console
git commit --amend -m "Nova mensagem"
```

Para desfazer o commit e retornar ao commit anterior, usamos o comando **git restore** que tem 3 opções:
1. soft: Ele desfaz os commits até o commit que você selecionou (usando o hash) e coloca esse arquivos no staging area
2. mixed: comportamento padrão, ele pega os arquivos anteriores e coloca e tira da staging area, os arquivos ficam untracked
3. hard: Ignora completamente os arquivos dos commits anteriores, é como se apagasse. 

O comando **git reflog** traz o histórico mais profundo.   
Repare que todos esses comandos são feitos antes do git push!

O comando **git pull** traz as alterações do repositório remoto para o repositório local


```console
git pull
```

### Branches

Uma Branch é uma ramificação do projeto. Ela é um ponteiro móvel para um commit no histórico do repositório. Quando se cria um anova branch a partir de outra existe, a nova se inicia apontando para o mesmo commit da branch que estava quando foi criada. Para criar uma branch fazemos


```console
git checkout -b novaBranch
```

E para retornar a branch main


```console
git checkout main
```

O commando **git branch -v** mostra o último commit de cada branch

```console
git branch -v
```

Podemos mesclar as branchs, isso possibilita que os arquivos e mudanças de uma branch passe para outra. No exemplo abaixo, dizemos que queremos mesclar na branch main a branch novaBranch


```console
git merge novaBranch
```

Por fim, podemos listar as branchs que temos no repositório e excluir a branch novaBranch:

```console
git branch
git branch -d novaBranch
```

Mas temos problemas de conflitos, e um deles é o **conflito de merge** que é quando temos alterações concorrentes, que é quando duas pessoas trabalham no mesmo repositório e alteram a mesma linha de código, quando um dos dois tenta enviar vai dar conflito com o que o outro enviou. Isso gera um conflito porque o git não sabe qual é o certo. Quando isso acontece, fazemos um **git pull** que trará todos os conlfitos e caberá a nós decidir qual a solução.

Por fim, temos o comando **git fetch**. O comando **git fetch** diz se houve alteração no repositório, antes de mesclar com sua branch local.

```console
git fetch main
git diff main origin/main
git merge origin/main
```

Quando queremos clonar apenas uma branch de um repositório com muitas branchs fazemos:

```console
git clone url --branch nome_branch --single-branch
```

O comando **git stash** arquiva as alterações para poder decidir o que fazer no futuro:


```console
git stash
git stash list
git stash pop/apply
```

Por fim, deve-se ler a documentação do git, disponivel em:
[Documentação Git](git-scm.com/docs)
[Documentação - Book](git-scm.com/book/en/v2)
