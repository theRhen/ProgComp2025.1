print("----------------------------------------")
print("         TAXA DO ESTACIONAMENTO")
print("----------------------------------------")
minutos = int(input("Digite a quantidade de minutos no estacionamento: "))

horas = minutos // 60 # Converte minutos em horas arredondando 
resto = minutos % 60
if resto != 0:
    horas = horas + 1

if horas > 12: # Verifica se passou de 12 horas
    valor = 30.00
else:
    valor = 0

    if horas >= 1: # Calcula o valor das duas primeiras horas
        valor = valor + 8.00
    if horas >= 2:
        valor = valor + 8.00

    if horas >= 3: # Calcula o valor da terceira e quarta horas
        valor = valor + 5.00
    if horas >= 4:
        valor = valor + 5.00

    if horas >= 5: # Calcula o valor das horas restantes, acima de 4
        valor = valor + (horas - 4) * 3.00

print("O valor a ser pago é: R$", valor)
print("----------------------------------------")
