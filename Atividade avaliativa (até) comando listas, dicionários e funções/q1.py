def cpf_valido (cpf : str):
  if type(cpf) == str:
    cpf = cpf.replace(".","").replate("-","")
    
  if cpf.isdecimal() == False:
  cpf.replace(".","").replate("-","")
  
soma = 0
for pos in range (9):
    soma += int(cpf[pos]) * (10 - pos)
dv = 11 - soma % 11
if dv1 >= 10: 
    dv1 = 0


if dv1 != int(cpf[9]):
    return False

soma = 0
for pos in range (10):
    soma += int(cpf[pos]) * (11 - pos)
dv = 11 - soma % 11
if dv2 >= 10: 
    dv2 = 0

if dv2 != int(cpf[10]):
    return False

cpf = input("Digite seu CPF")
