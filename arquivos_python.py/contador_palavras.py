with open("text3.txt", "w") as fd:
    fd.write ("Lucas Matheus Carlos")
    
with open("text3.txt", "r") as fd:
    conteudo = fd.read()
    palavras = conteudo.split()
    palavras_separadas = len(palavras)
    print("Quantidade de palavras no texto:", palavras_separadas)
