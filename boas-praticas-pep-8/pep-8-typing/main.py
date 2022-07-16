# from fila_normal import filanormal
from fila_prioritaria import FilaPrioritaria


# Exemplos de código sem padrões
# fila_teste = filanormal()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# print(fila_teste.chamacliente(5))
# print(fila_teste.chamacliente(10))



# Exemplos de código com PEP-8 e Type hints
fila_teste_2 = FilaPrioritaria()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
print(fila_teste_2.chama_cliente(5))
print(fila_teste_2.chama_cliente(1))
print(fila_teste_2.estatistica('10/01/1993', 198, 'detail'))
