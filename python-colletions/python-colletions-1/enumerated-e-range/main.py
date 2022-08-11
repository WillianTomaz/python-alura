idades = [15, 87, 32, 65, 56, 32, 49, 37]


# Exemplo de listagem com Range:
print("------------------------------------")
print(f"RANGE => {range(len(idades))}")
print(f"RANGE (LIST) => {list(range(len(idades)))}") # forçando a geração dos valores

for i in range(len(idades)):
  print(f"RANGE (FOR) => {i, idades[i]}")





# Exemplo de listagem com enumerate (retorna do tipo TUPLA):
print("------------------------------------")
print(f"ENUMERATE (LIST) => {list(enumerate(idades))}") # Pega tudo de uma vez

for indice, idade in enumerate(idades): # Deste modo fica como Lazy e vai gerando(pegando valor) conforme a iteração
  print(f"ENUMERATE (FOR) => {indice} {idade}") # Fazendo unpacking da tupla




# Exemplo desempacotando TUPLA:
print("------------------------------------")
usuarios = [
  ("Guilherme", 37, 1991),
  ("Daniela", 31, 1987),
  ("Paulo", 39, 1979)
]

for nome, idade, nascimento in usuarios: # Deixando explícito os três elementos
  print(f"Nome: => {nome}") # Fazendo unpacking da tupla

# Nesse caso abaixo o _ (underline) ignora as posições (nome, idade, nascimento) 
# for nome, _, _ in usuarios: 
  # print(f"Nome: => {nome}") # Fazendo unpacking da tupla

