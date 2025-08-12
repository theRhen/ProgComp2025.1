with open("text2.txt", "w") as fd:
    for i in range(1,11):
        fd.write(f"Linha {i}\n")

with open("text2.txt", "r") as fd:
    texto = fd.read()
    print(texto)
