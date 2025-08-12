with open("text.txt", "w") as fd:
    fd.write("Arquivo criado com sucesso!\n")
    
with open("text.txt", "a") as fd:
    fd.write("Essa e a primeira linha do texto")

with open("text.txt", "r") as fd:
    texto = fd.read()
    print(texto)
