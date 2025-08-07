def func_palindromo(n):
    x = n
    invertido = 0

    while n > 0:
        resto = n % 10
        invertido = invertido * 10 + resto
        n = n // 10

    return x == invertido

contador = 0

for numero in range(10, 100001):

    if func_palindromo(numero):
        contador += 1

print("Total de palíndromos:", contador)
