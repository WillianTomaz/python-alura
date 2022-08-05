from extrator_url import ExtratorURL

# extrator_url = ExtratorURL("  ")
extrator_url = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
print("Tamanho da URL:", len(extrator_url))

valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)
