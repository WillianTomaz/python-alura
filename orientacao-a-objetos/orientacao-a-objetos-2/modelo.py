class Programa:
  def __init__(self, nome, ano):
    self._nome = nome.title()
    self.ano = ano
    self._likes = 0

  @property
  def nome(self):
    return self._nome
  
  @nome.setter
  def nome(self, novo_nome):
    self._nome = novo_nome.title()
  
  @property
  def likes(self):
    self._likes += 1

  def dar_likes(self):
    self._likes += 1

class Filme (Programa):
  def __init__(self, nome, ano, duracao):
    super().__init__(nome, ano)
    self.duracao = duracao

class Serie (Programa):
  def __init__(self, nome, ano, temporadas):
    super().__init__(nome, ano)
    self.temporadas = temporadas


vingadores = Filme('vingadores - gerra infinita', 2018, 160)
vingadores.dar_likes()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
      f'- Duração: {vingadores.duracao} - Temporada: {vingadores.likes}')


atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} '
      f'- Temporada: {atlanta.temporadas} - Temporada: {atlanta.likes}')