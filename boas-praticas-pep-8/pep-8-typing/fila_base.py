import abc

# Exemplos de código com PEP-8 e Type hints

class FilaBase(metaclass=abc.ABCMeta):
  codigo: int = 0
  fila = []
  clientes_atendidos = []
  senha_atual: str = ""
  
  def reseta_fila(self) -> None:
    if self.codigo >= 200:
      self.codigo = 0
    else:
      self.codigo += 1

  @abc.abstractmethod
  def gera_senha_atual(self) -> None:
    ...

  @abc.abstractmethod
  def atualiza_fila(self) -> None:
    ...

  @abc.abstractmethod
  def chama_cliente(self, caixa: int) -> None:
    ...
