from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta):

  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0

  def deposita(self, valor):
    self._saldo += valor

  # Forçando a implementação 
  # se não fazer implementação do método, 
  # na hora de instaciar vai dar erro
  @abstractmethod
  def passa_o_mes(self):
    pass

  def __str__(self):
    return f"Codigo: {self._codigo} | Saldo: {self._saldo}"


