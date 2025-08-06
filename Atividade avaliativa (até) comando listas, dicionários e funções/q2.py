# Função para verificar se um número é palíndromo (sem usar strings)
def eh_palindromo(n):
    original = n         # Armazena o valor original
    invertido = 0        # Vai guardar o número invertido

    while n > 0:
        digito = n % 10              # Pega o último dígito
        invertido = invertido * 10 + digito  # Constrói o número invertido
        n = n // 10                  # Remove o último dígito

    return invertido == original     # Retorna True se for palíndromo

# Programa principal
def contar_palindromos():
    try:
        contador = 0

        # Verifica todos os números de 10 até 100000 (inclusive)
        for numero in range(10, 100001):
            if eh_palindromo(numero):
                contador += 1

        print("Quantidade de números palíndromos entre 10 e 100000:", contador)

    except Exception as e:
        print("Ocorreu um erro:", e)

# Executa o programa
contar_palindromos()
