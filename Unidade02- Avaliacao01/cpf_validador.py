# Riquelme Henrique da Silva Ferreira

# Validador CPF gbat
def cpf_valido (cpf : str):
    
    if type(cpf) != str: 
        print("Erro: O CPF deve ser uma string.")
        return False
    
    cpf = cpf.replace(".", "").replace("-", "")
    
    if cpf.isdecimal() == False:
        print("Erro: O CPF deve conter apenas números.")
        return False
    
    if len(cpf) != 11:
        print("Erro: O CPF deve ter 11 dígitos.")
        return False
    
    soma = 0
    for pos in range (9):
        soma += int(cpf[pos]) * (10 - pos)
    dv1 = 11 - soma % 11
    if dv1 >= 10: dv1 = 0
        
    if dv1 != int(cpf[9]):
        return False
    
    soma = 0
    for pos in range (10):
        soma += int(cpf[pos]) * (11 - pos)
    dv2 = 11 - soma % 11
    if dv2 >= 10: dv2 = 0
        
    if dv2 != int(cpf[10]):
        return False
    
    return True
  
#cpf = input ("Digite seu CPF (xxx.xxx.xxx-xx): ")
#print ("CPF é valido:", cpf_valido(cpf))  
