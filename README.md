# receitas-da-minha-avo
As melhores receitas da minha vovozinha

# padrão das mensagens de commits deste repositório:

add: uma nova receita foi adicionada
feat: uma nova funcionalidade foi implementada
fix: um erro foi corrigido
break: uma mudança que impede a construção do projeto foi introduzida
doc: documentação sobre o projeto foi inserida
refac: reescreve/refatora o código para melhor legibilidade ou organização

# resumo dos comandos git

Comandos de introspecção. Saber o estado atual, listar commits e verificar diferenças entre versões.

```bash
git status
git log
git diff <arquivo1>
git diff <branch1> <branch2>
```

Adicionar mudanças realizadas.

```bash
git add <arquivo1> .. <arquivo2> .. 
```

Registrar no repositório as mudanças adicionadas.
```bash
git commit -m "<nosso código padrão>: <sua breve mensagem>"
```

Criar braços e listar braços.
```bash
git branch <nome-do-braço>
git branch
```

Comando de movimentação. Sair de um braço e ir para outro.
```bash
git checkout <nome-do-braço>
```

Mandar o seu trabalho commitado para a nuvem.


```bash
git push <nome do braço remoto> <nome do braço local>
git push origin main
```

Braço atual
```bash
git push
```