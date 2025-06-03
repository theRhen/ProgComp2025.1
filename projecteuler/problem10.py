soma = 2 + 3
for n in range (4, 2000000):
    ehprimo = True
    for div in range (2, int(n**0.5) + 1):
        if n % div == 0:
            ehprimo = False
            break
    if ehprimo:
        soma += n
    if n % 10000 == 0:
        print(n)
    print(soma)
