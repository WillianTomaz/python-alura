from functools import total_ordering


@total_ordering
class ContaSalario:

  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0

  def deposita(self, valor):
    self._saldo += valor

  def __str__(self):
    return f"Codigo: {self._codigo} | Saldo: {self._saldo}"

  def __eq__(self, outro):
    if type(outro) != ContaSalario:
      return False

    return self._codigo == outro._codigo and self._saldo == outro._saldo


  def __lt__(self, outro):
    if self._saldo != outro._saldo:
      return self._saldo < outro._saldo

    return self._codigo < outro._codigo
