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

  def __str__(self):
    return f'{self._nome} - {self.ano} - {self._likes} Likes'