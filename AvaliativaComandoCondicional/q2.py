print("----------------------------------------")
print(" CALCULADORA SITUAÇÃO DE APROVAÇÃO IFRN")
print("----------------------------------------")

n1 = float(input("Digite sua nota do primeiro bimestre: ")) # n1 = nota primeira unidade
n2 = float(input("Digite sua nota do segundo bimestre: ")) # n1 = nota segunda unidade

media = (n1*2 + n2*3) / 5 # media = n1 peso 2 + n2 peso 3
print("........................................")
print("           Sua média é:", media)
print("........................................")

if media >= 60: # Nota maior ou igual 60 = Aluno aprovado direto
    print("Situação do aluno: APROVADO")
    print("----------------------------------------")
    
if 20 <= media < 60: # Media entre 20 e 59.9 = Aluno em prova final
    print("Situação do aluno: PROVA FINAL")
    nota_final = float(input("Digite sua nota da prova final: "))
    media_final = (media + nota_final) / 2
    
    if media_final >= 60: # Media final maior ou igual a 60 = Aluno aprovado
        print("Situação do aluno: APROVADO")
        print("----------------------------------------")
    else: # Media final não maior ou igual a 60 = Aluno reprovado
        print("Situação do aluno: REPROVADO")
        print("----------------------------------------")
    
if media < 20: # Nota menor que 20 = Aluno reprovado direto
    print("Situação do aluno: REPROVADO")
    print("----------------------------------------")
    

    
    
