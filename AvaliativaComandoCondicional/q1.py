print("----------------------------------------")
print("   SOMADOR DE ALGORISMOS DE 4 DIGITOS")
print("----------------------------------------")

numero = int(input("Digite um número menor que 10000: "))

if 0 < numero < 10000:

    digito1 = numero//1000 # 1234//1000 = [1],234 ("1" primeiro digito)
    resto = numero % 1000 # 1234 % 1000 = 234 ("234" resto dos digitos)

    digito2 = resto//100 # 234//100 = [2],34 ("2" segundo digito)
    resto = resto % 100 # 234 % 100 = 34 ("34" resto dos digitos)

    digito3 = resto//10 # 34//10 = [3],4 ("3" segundo digito)
    resto = resto % 10 # 34 % 10 = 4 ("4" resto dos digitos)

    digito4 = resto//1 # 4//1 = [4] ("4" segundo digito)
    
    soma = (digito1 + digito2 + digito3 + digito4) # soma = 1 + 2 + 3 + 4
    
    print("A soma é:", digito1, "+", digito2, "+", digito3, "+", digito4, "=", soma) # 10
    print("---------------------------------------")
    
else:
    print("O valor deve ser menor que 10000")
    print("---------------------------------------")

