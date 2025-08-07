# Validador MAC
def mac_valido(mac: str):    
    if type(mac) != str:
        print("\nErro: O MAC deve ser uma string.")
        return False
    
    mac = mac.replace(":", "").replace(".", "").replace("-", "")
    
    if len(mac) != 4:
        print("\nErro: O MAC deve ter 4 dígitos.")
        return False
    
    if mac.isalnum() == False: 
        print("\nErro: O MAC deve conter apenas letras e números.")
        return False
    return True

#mac = input ("Digite seu MAC (xx-xx): ")
#print ("MAC é valido:", mac_valido(mac))  
