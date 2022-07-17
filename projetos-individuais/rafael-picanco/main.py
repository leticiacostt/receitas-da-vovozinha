titulo = 'hello world, my friend'
numero_palavras_titulo = len(titulo.split())

# lógica condicional baseada em valores boleanos
mostrar_variaveis = False
# if (numero_palavras_titulo > 4):
#   print('1: O valor das variáveis é:')
#   print(titulo, numero_palavras_titulo)
# else:
#   print('2: O valor das variáveis não será mostrado.')

# laços de repetição

# for == repeat: executa primeiro e depois testa
lista_de_numeros = []
for i in range(0, 10):
  lista_de_numeros.append(i)
  if len(lista_de_numeros) > 0:
    break

# o while testa primeiro e depois executa
i = 0
while True:
  lista_de_numeros.append(i)
  i += 1

# for simples só executa e não testa nada
lista_de_numeros = [i for i in range(0, 100)]
print(lista_de_numeros)