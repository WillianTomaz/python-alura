from extrator_url import ExtratorURL

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)

print("(URL) Tamanho:", len(extrator_url))
print(extrator_url)

nome_parametro = "quantidade"
valor_parametro = extrator_url.get_valor_parametro(nome_parametro)
print(f"(URL) Valor '{valor_parametro}' do Parametro '{nome_parametro}'.")


extrator_url2 = ExtratorURL(url)
print("(URL) São iguais:", extrator_url == extrator_url2)