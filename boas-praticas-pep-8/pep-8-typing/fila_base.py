import abc

from constants import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO

# Exemplos de código com PEP-8 e Type hints

class FilaBase(metaclass=abc.ABCMeta):
  codigo: int = 0
  fila = []
  clientes_atendidos = []
  senha_atual: str = ""
  
  def reseta_fila(self) -> None:
    if self.codigo >= TAMANHO_PADRAO_MAXIMO:
      self.codigo = TAMANHO_PADRAO_MINIMO
    else:
      self.codigo += 1

  def inseri_cliente(self):
    self.fila.append(self.senha_atual) 

  @abc.abstractmethod
  def gera_senha_atual(self) -> None:
    ...

  def atualiza_fila(self) -> None:
    self.reseta_fila()
    self.gera_senha_atual()
    self.inseri_cliente()

  @abc.abstractmethod
  def chama_cliente(self, caixa: int) -> None:
    ...
