class Conta:

  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0

  def deposita(self, valor):
    self._saldo += valor

  def __str__(self):
    return f"Codigo: {self._codigo} | Saldo: {self._saldo}"

