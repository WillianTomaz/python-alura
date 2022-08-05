from extrator_url import ExtratorURL

extrator_url = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
print("(URL) Tamanho:", len(extrator_url))
print(extrator_url)

nome_parametro = "quantidade"
valor_parametro = extrator_url.get_valor_parametro(nome_parametro)
print(f"(URL) Valor '{valor_parametro}' do Parametro '{nome_parametro}'.")
