# Riquelme Henrique da Silva Ferreira
# Validador MAC
def mac_valido(mac: str):    
    if type(mac) != str:
        print("\nErro: O MAC deve ser uma string.")
        return False
    
    mac = mac.replace(":", "").replace(".", "").replace("-", "")
    
    if len(mac) != 12:
        print("\nErro: O MAC deve ter 12 dígitos.")
        return False
    
    if mac.isalnum() == False: 
        print("\nErro: O MAC deve conter apenas letras e números.")
        return False
    return True

#mac = input ("Digite seu MAC (xx-xx-xx-xx-xx-xx): ")
#print ("MAC é valido:", mac_valido(mac))  
