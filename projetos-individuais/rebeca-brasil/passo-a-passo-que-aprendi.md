Comandos - com o objetivo de realizar uma cópia do código; fazer alterações; enviar as modificações e atualizar o programa.

# 1.A partir de um repositório já existente pedir uma cópia para trabalhar – FORK
# 2.Clonar o código para trabalhar com ele
# 3. Entrar na pasta
# 4. Criar um braço de segurança, para alterar sem modificar o braço principal (main) original. Posteriormente ele pode ser apagado, quando as alterações forem enviadas para o autor
# 5.Enviar sua alteração local para o autor atualizá-la no repositório e ficar sincronizada posteriormente. – COMMIT e PULL REQUEST
# 6.1.Se quiser continuar trabalhando você pode Atualizar para o seu repositório as alterações aceitas pelo autor - GIT PULL UPSTREAM MAIN.
# 6.2. Sincronizar as alterações do seu repositório local com a sua versão web. GIT PUSH
# Fim 

Tentei descrever cada uma dessas etapas:

# 1.A partir de um repositório já existente pedir uma cópia para trabalhar – FORK
-No github web clicar em FORK; Clicar em create a new fork no git hub web; vc pode abrir o código no github dekstop se ele pedir

# 2.Clonar o código para trabalhar com ele
-no github dekstop escolher a opção clonar.

# 3. Entrar na pasta através do git bash (escrever depois do $)
-$ ls + enter (serve para listar as pastar)
-$ cd nome da pasta (que se quer entrar)
–	listar e entrar na pasta até entrar na pasta que vai usar.
–	Obs: para retorna em uma pasta pode usar (cd+espaço+..+enter) ou seja(cd ..)
Descrevi minhas pastas no tópico 6.1

# 4. Criar um braço de segurança, para alterar sem modificar o braço principal (main) original. Posteriormente ele pode ser apagado, quando as alterações forem enviadas para o autor
   –	Caso faça as alterações antes de criar um braço, será necessário criar um novo braço; mesclá-lo (git merge) com o principal; fazer o envio para o autor e só depois excluir o braço novo. Se fizer o braço primeiro segue as etapas:

-entrar na pasta escolhida (cd nome da pasta) –lembrar não usa espaço, mas (-)
-git branch (para listar os braços)
-git branch nome do braço (novo que quer criar)
-git branch (para verificar se o braço foi criado)
-git checkout nome do braço (para entrar no braço criado) pode apertar TAB para completar automaticamente o nome da página e não ter que escrever tudo.
   –	O vscode já reconhece que vc está no braço e indica na parte inferior esquerda com um simbolo de ramificação. 

# 5.Enviar sua alteração local para o autor atualizá-la no repositório e ficar sincronizada posteriormente. – COMMIT e PULL REQUEST
   –	Fazer alterações no VSCode
   –	Dentro do VSCode fazer o commit (finalizar a escrita para enviar e assim registrar no repositório as mudanças )

-procurar um símbolo de ramificação (controle do código fonte) nessa versão fica na barra lateral esquerda inferior ao símbolo de lupa
-.Em alterações clicar no símbolo de mais (+) ao lado do seu arquivo, para adicionar as alterações.
-Inserir um código de mensagem que foi proposto no arquivo README (ex: add, doc:; ...) junto com uma mensagem sobre o que é a alteração (ex: fix: correção palavra)
-Nesse momento estamos escolhendo apenas a opção commit
-escrever novamente a mensagem e clicar em “publica final”
-Como estamos usando o código do autor escolher a opção: origin com o seu nome do git hub e não o upstream com nome do professor.
-sincronizar alterações

   –	Abrir o github desktop lá aparece que você tem um novo braço pronto para ser publicado.
-clicar em create pull request
-no navegador na sua página com seu nome de usuário confirmar o create pull request (pode aparecer em verde)
   –	Vai aparecer (nome-de-usuário wants to merge 1 commit into nome de usuário do autor from seu nome de usuário) confirmando o procedimento.
   –	Pode aparecer uma mensagem indicando que NÃO Há conflitos (em verde) ou que HÁ conflitos (em verde); nesse caso o professor recebeu as suas alterações e ficou responsável por resolver os conflitos.  

# 6.1.Se quiser continuar trabalhando você pode Atualizar para o seu repositório as alterações aceitas pelo autor - GIT PULL UPSTREAM MAIN.
   –	Você precisa encontrar a pasta para alterar, pode escrevê-la direto 
(ex: cd /Documents/GitHub/receitas-da-vovozinha), 
mas vou abrir e listar uma pasta de cada vez:

-$ ls + enter (serve para listar as pastar)
-$ cd nome da pasta (que se quer entrar)
–	listar e entrar na pasta até entrar na pasta que vai usar.
–	Obs: para retorna em uma pasta pode usar (cd+espaço+..+enter) ou seja(cd ..)
No meu:
-$ ls (enter) para listar as pastas
-$ cd Documents (enter) para selecionar pasta documentos –onde meu git hub está
-$ ls ( enter) para listar dentro de documents
-$ cd github (enter) para entrar na pasta github
-$ ls (enter) para listar dentro do github
-$ cd receitas-da-vovozinha/ (enter) para entrar na pasta de receitas; pode começar a escrever e usar TAB para completar a frase sem precisar escrever tudo manualmente.

   –	Caso precise mudar de braço pode usar o (git checkout nome do braço) 
Ex: “braço qualquer” e quero ir para “braço principal das receitas” (git checkout nome do braço) ou seja (git checkout main)
   –	Depois de encontrar a pasta pode finalmente atualizar

-$ git pull upstream (nome do braço) ou seja (git pull upstream main) esse comando permite “puxar” as atualizações que o autor fez para sua máquina local.

   Agora é necessário sincronizar o local com a sua nuvem na web.   

# 6.2. Sincronizar as alterações do seu repositório local com a sua versão web. GIT PUSH
-$ git push (para sincronizar o local com a sua própria nuvem “enviar”)

# Fim 
