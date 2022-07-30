class Filme:
  def __init__(self, nome, ano, duracao):
    self.nome = nome.title()
    self.ano = ano
    self.duracao = duracao
    self.likes = 0

  def dar_likes(self):
    self.likes += 1

class Serie:
  def __init__(self, nome, ano, temporadas):
    self.nome = nome.title()
    self.ano = ano
    self.temporadas = temporadas
    self.likes = 0

  def dar_likes(self):
    self.likes += 1


vingadores = Filme('vingadores - gerra infinita', 2018, 160)
vingadores.dar_likes()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
      f'- Duração: {vingadores.duracao} - Temporada: {vingadores.likes}')


atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} '
      f'- Temporada: {atlanta.temporadas} - Temporada: {atlanta.likes}')