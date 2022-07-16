from fila_base import FilaBase

# Exemplos de código sem padrões

class filanormal(FilaBase):

  def gerasenhaatual(self)->None:
    self.senhaatual = f'NM{self.codigo}'

  def atualizafila(self)->None:
    self.reseta_fila()
    self.gerasenhaatual()
    self.fila.append(self.senhaatual)

  def chamacliente(self, caixa:int)->str:
    cliente_atual:str = self.fila.pop(0)
    self.clientesatendidos.append(cliente_atual)
    return(f'Cliente atual: {cliente_atual} dirija-se ao caixa: {caixa}')