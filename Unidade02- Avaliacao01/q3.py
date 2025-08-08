import random

# Lista de palavras válidas
palavras = (
    "ADAGA", "ADUBO", "AMIGO", "ANEXO", "ARAME", "ARARA", "ARROZ",
    "ASILO", "ASTRO", "BAILE", "BAIXA", "BALAO", "BALSA", "BARCO",
    "BARRO", "BEIJO", "BICHO", "BORDA", "BORRA", "BRAVO", "BREJO",
    "BURRO", "CAIXA", "CALDO", "CANJA", "CARRO", "CARTA", "CERVO",
    "CESTA", "CLIMA", "COBRA", "COLAR", "COQUE", "COURO", "CRAVO",
    "DARDO", "FAIXA", "FARDO", "FENDA", "FERRO", "FESTA", "FLUOR",
    "FORCA", "FORNO", "FORTE", "FUNDO", "GAITA", "GARRA", "GENIO",
    "GESSO", "GRADE", "GRANA", "GRAMA", "GURIA", "GREVE", "GRUTA",
    "HEROI", "HOTEL", "ICONE", "IMPAR", "IMUNE", "INDIO", "JUNTA",
    "LAPIS", "LARVA", "LAZER", "LENTO", "LESTE", "LIMPO", "LIVRO",
    "MACIO", "MAGRO", "MALHA", "MANSO", "MARCO", "METAL", "MORTE",
    "MORRO", "MURAL", "MOVEL", "NACAO", "NINHO", "NOBRE", "NORMA",
    "NORTE", "NUVEM", "PACTO", "PALHA", "PARDO", "PARTE", "PEDRA",
    "PEDAL", "PEIXE", "PRADO", "PISTA", "POMBO", "POETA", "PONTO",
    "PRATO", "PRECO", "PRESO", "PROSA", "PRUMO", "PULGA", "PULSO",
    "QUEPE", "RAIVA", "RISCO", "RITMO", "ROSTO", "ROUPA", "SABAO",
    "SALTO", "SENSO", "SINAL", "SITIO", "SONHO", "SOPRO", "SURDO",
    "TARDE", "TERNO", "TERMO", "TERRA", "TIGRE", "TINTA", "TOLDO",
    "TORRE", "TRAJE", "TREVO", "TROCO", "TRONO", "TURMA", "URUBU",
    "VALSA", "VENTO", "VERDE", "VISAO", "VINHO", "VIUVO", "ZEBRA"
)

# Função para colorir as letras
def colorir(palpite, palavra):
    resultado = ""
    for i, letra in enumerate(palpite):
        if letra == palavra[i]:
            resultado += f"\033[1;37;42m{letra}\033[m"  # verde
        elif letra in palavra:
            resultado += f"\033[1;37;43m{letra}\033[m"  # amarelo
        else:
            resultado += f"\033[1;37;40m{letra}\033[m"  # cinza
    return resultado

# Escolher as duas palavras diferentes
palavra1 = random.choice(palavras)
palavra2 = random.choice(palavras)
while palavra2 == palavra1:
    palavra2 = random.choice(palavras)

tentativas = 7
acertou1 = False
acertou2 = False

print("-------------------------------------------------")
print("           Bem-vindo ao Termo Dueto!")
print("-------------------------------------------------")
print("Você tem 7 tentativas para acertar as 2 palavras.")
print("As palavras têm 5 letras. Boa sorte!")
print("-------------------------------------------------")

for rodada in range(1, tentativas + 1):
    print(f"\nTentativa {rodada}/{tentativas}")
    palpite = input("Digite uma palavra: ").strip().upper()

    if palpite not in palavras:
        print("❌ Palavra inválida! Escolha uma da lista de palavras permitidas.")
        continue

    # Mostrar resultado para cada palavra
    if not acertou1:
        print("Palavra 1:", colorir(palpite, palavra1))
    else:
        print("Palavra 1: ✅")

    if not acertou2:
        print("Palavra 2:", colorir(palpite, palavra2))
    else:
        print("Palavra 2: ✅")

    # Atualizar acertos
    if palpite == palavra1:
        acertou1 = True
    if palpite == palavra2:
        acertou2 = True

    # Checar vitória
    if acertou1 and acertou2:
        print("\n🎉 Parabéns! Você acertou as duas palavras!")
        break
else:
    print("\n❌ Suas tentativas acabaram.")
    print(f"As palavras eram: {palavra1} e {palavra2}")
