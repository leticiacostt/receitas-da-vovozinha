# receitas-da-minha-avo
As melhores receitas da minha vovozinha

# padrão das mensagens de commits deste repositório:

Os códigos a seguir são apenas uma convenção que nos usaremos para facilitar o a escrita de mensagens de commit.

Atenção para o formato:

    código - dois pontos e espaço - mensagem

add: uma nova receita foi adicionada   
feat: uma nova funcionalidade foi implementada  
fix: um erro foi corrigido  
break: uma mudança que impede a construção do projeto foi introduzida  
doc: documentação sobre o projeto foi inserida  
refac: reescreve/refatora o código para melhor legibilidade ou organização  

# Resumo dos comandos git

## Comandos de introspecção

Checar o estado atual de modificações.
```bash
git status
```

Listar commits.
```bash
git log
```

verificar diferenças entre versões de um arquivo.
```bash
git diff <arquivo1>
git diff <branch1> <branch2>
```

## Comandos de registro no histórico do repositório

Adicionar mudanças realizadas.
```bash
git add <arquivo1> .. <arquivo2> ..
```

Registrar no repositório as mudanças adicionadas.
```bash
git commit -m "<nosso código padrão>: <sua breve mensagem>"
```

## Comandos de manejo e movimentação dentro do repositório

Criar um novo braço (área de trabalho) tendo como base a área de trabalho atual.
```bash
git branch <nome-do-braço>
```

Listar braços disponíveis localmente.
```bash
git branch <nome-do-braço>
```

Sair do braço atual e ir para um outro braço alvo.
```bash
git checkout <nome-do-braço-alvo>
```

## Comandos para sincronizar mudanças entre seu repositório local e seu repositório na nuvem

Lembre que o seu repositório Git com o seu código existe localmente (no seu computador) e remotamente (em um computador na nuvem, servido pelo GitHub no nosso caso). Mudanças precisam ser sincronizadas entre esses dois computadores.

Enviar para a nuvem um novo braço criado localmente.
```bash
git push origin main <nome-do-braço>
```

Enviar braço atual para a nuvem.
```bash
git push
```

## Comandos e tarefas para trabalhar colaborativamente

### Tarefa 1. Fazer uma cópia local de um projeto original de outra pessoa.

**Passo 1**. Acessar o endereço do projeto original, no nosso caso:   
https://github.com/cpicanco/receitas-da-vovozinha

**Passo 2**. Crie uma cópia na nuvem do projeto original associada à sua conta: apertar no botão "fork" localizado no canto superior direito da página principal do projeto.

**Passo 3**. Crie uma cópia local do seu `fork` (sua cópia na nuvem do projeto original): Acesse o GitHub Desktop e escolha a opção "Clone repository" e escolha <seu-login-no-github>/receitas-da-vovozinha, atualize a lista de repositório se necessário.

Os passos seguintes são necessários caso sua cópia remota não esteja sincronizada com o repositório do professor.

**Passo 4**. Abra o Git Bash.

**Passo 5**. Navegue até a pasta do repositório no seu computador, por exemplo:

```bash
cd /Documents/GitHub/receitas-da-vovozinha
git pull upstream main
```

**Nota**: o local da pasta do repositório no seu computador pode ser diferente, você pode conferir o local da pasta usando o GitHub Desktop: aperte o botão direito do mouse em cima do nome do repositório e em seguida escolha "Show in Explorer".

**Passo 6**. Sincronize o seu repositório local com o repositório remoto do professor:
```bash
git pull upstream main
```

**Nota**: o comando `git pull upstream main` significa "Git, puxe do repositório remoto do professor o braço main e misture ele com meu braço atual local"

**Passo 7**. Sincronize o seu repositório local com sua cópia remota:
```bash
git push
```

### Tarefa 2: Enviar suas mudanças locais para o repositório original do professor.

**Passo 1**: Após fazer o `commit` de suas mudanças em seu repositório local, envie elas em um novo braço para a nuvem:

```bash
git branch minhas-mudancas
git push origin minhas-mudancas
```

**Passo 2**: Acesse sua página do repositório no GitHub na Web e, escolha a aba "branchs" e aperte em "Create Pull Request"

**Passo 3**: Aguarde o professor aceitar as mudanças e incorporá-las no projeto original.
  
# ciclo de trabalho
- criar um novo braço (git branch nome do braço)
- fazer as alterações
- salvar as alterações (ctrl+s)
- adicionar uma mensagem sobre o que foi alterado (add: nome da alteração)
- fazer o envio (commit)
- na nuvem realizar o (pull request)

## Mesclar braços 
- buscar o braço (git branch) 
- fazer alterações no braço (git checkout)
- escolher o braço para mesclar (git merge nome do braço)  
- deletar o braço se não for mais usar (branch -d nome do braço )

# .gitignore

Video: https://www.youtube.com/watch?v=UR9X2VBECE4&ab_channel=WillianJusten

- Um arquivo `.gitignore` contém uma lista de arquivos. Ele pode ser criado em qualquer diretório e diz para o `git` que os arquivos listados devem ser ignorados. Ou seja, ele e suas modificações não serão rastreadas. Isso é útil porque ao do processo de desenvolvimento muitos arquivos temporários, reduldantes ou irrelevantes são criados e devem ser ignorados. Um exemplo concreto é o caso de arquivos executáveis. Eles são grandes e possuem um formato binário, em vez de texto puro como nos arquivos do código fonte, sendo, portanto, incompatíveis com a lógica de funcionamento do `git`.