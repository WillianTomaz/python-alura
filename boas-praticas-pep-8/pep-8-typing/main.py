from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida

# Exemplos de código com PEP-8 e Type hints


### Fila Normal ###
# teste_fabrica = FabricaFila().pega_fila(tipo_fila='normal')
# teste_fabrica.atualiza_fila()
# teste_fabrica.atualiza_fila()
# teste_fabrica.atualiza_fila()
# print(teste_fabrica.chama_cliente(12))
# print(teste_fabrica.chama_cliente(12))
# print(teste_fabrica.chama_cliente(12))




### Fila Prioritaria ###
teste_fabrica = FabricaFila().pega_fila(tipo_fila='prioritaria')
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(12))
print(teste_fabrica.chama_cliente(12))
print(teste_fabrica.chama_cliente(12))
print(teste_fabrica.estatistica('10/01/1993', 198, EstatisticaDetalhada))
