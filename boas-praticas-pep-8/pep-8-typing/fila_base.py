# Exemplos de código com PEP-8 e Type hints

class FilaBase:
  codigo: int = 0
  fila = []
  clientes_atendidos = []
  senha_atual: str = ""
  
  def reseta_fila(self) -> None:
    if self.codigo >= 200:
      self.codigo = 0
    else:
      self.codigo += 1
