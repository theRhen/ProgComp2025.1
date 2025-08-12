from cpf_validador import cpf_valido # importar o arquivo do validador de CPF
from mac_validador import mac_valido # importar o arquivo do validador de MAC
import json

# Dicionário para armazenar os dados: CPF como chave, lista de MACs como valor
banco_dados = {}

# Loop principal
while True:
    print(" ----------------------------------------------------------------------- ")
    print("|                            MENU DE OPÇÕES                             |")
    print(" ----------------------------------------------------------------------- ")
    print(" ----------------------------------------------------------------------- ")
    print("| 1 - Cadastrar CPF                                                     |")
    print("| 2 - Adicionar MAC address a um CPF                                    |")
    print("| 3 - Remover um MAC address de um CPF                                  |")
    print("| 4 - Remover o CPF                                                     |") # só permitir se não existirem MAC addresses vinculados
    print("| 5 - Listar os CPFs cadastrados                                        |")
    print("| 6 - Listar os MAC addresses vinculados a um CPF                       |")
    print("| 7 - Salvar o banco de dados em um arquivo                             |")
    print("| 8 - Ler o banco de dados de um arquivo                                |")
    print("| 9 - Sair                                                              |")
    print(" ----------------------------------------------------------------------- ")

    opcao = input("Digite a opção de menu desejada: ")

    if opcao.isdigit() and 0 < int(opcao) < 10:
        opcao = int(opcao)

        if opcao == 1:
            print("\nVocê escolheu: 1 - Cadastrar CPF")
            
            cpf_input = input("Digite o CPF para cadastrar: ").strip()
                
            if cpf_valido(cpf_input) == False:
                print("\nCPF inválido! Tente novamente.")
            else:
                cpf_limpo = cpf_input.replace(".", "").replace("-", "")
                
                if cpf_limpo in banco_dados:
                    print(f"CPF {cpf_limpo}: já estava cadastrado no sistema.")
                else:
                    banco_dados[cpf_limpo] = []
                    print(f"CPF {cpf_limpo}: cadastrado com sucesso!")

        if opcao == 2:
            print("\nVocê escolheu: 2 - Adicionar MAC address a um CPF")

            cpf_input = input("Digite o CPF para vicular ao MAC: ").strip()

            if cpf_valido(cpf_input) == False:
                print("CPF inválido!")
            else:
                cpf_limpo = cpf_input.replace(".", "").replace("-", "")

                if cpf_limpo not in banco_dados:
                    print(f"CPF {cpf_limpo}: não cadastrado.")
                else:
                    mac = input("Digite o MAC address: ").strip()

                    if mac_valido(mac) == False:
                        print("MAC address inválido!")
                    else:
                        if mac in banco_dados[cpf_limpo]:
                            print("Este MAC já está vinculado a esse CPF.")
                        else:
                            banco_dados[cpf_limpo].append(mac)
                            print(f"MAC {mac} -> CPF {cpf_input}: vinculado com sucesso!")
            
        if opcao == 3:
            print("\nVocê escolheu: 3 - Remover um MAC address de um CPF")

            cpf_input = input("Digite o CPF: ").strip()

            if cpf_valido(cpf_input) == False:
                print("CPF inválido!")
            else:
                cpf_limpo = cpf_input.replace(".", "").replace("-", "")

                if cpf_limpo not in banco_dados:
                    print("CPF não está cadastrado.")
                else:
                    mac = input("Digite o MAC address a ser removido: ").strip()

                    if mac_valido(mac) == False:
                        print("MAC inválido.")
                    else:
                        if mac in banco_dados[cpf_limpo]:
                            banco_dados[cpf_limpo].remove(mac)
                            print("MAC removido com sucesso.")
                        else:
                            print("Este MAC não está vinculado a esse CPF.")

        if opcao == 4:
            print("\nVocê escolheu: 4 - Remover o CPF")
            
            cpf_input = input("Digite o CPF a ser removido: ").strip()

            if cpf_valido(cpf_input) == False:
                print("CPF inválido!")
            else:
                cpf_limpo = cpf_input.replace(".", "").replace("-", "")

                if cpf_limpo not in banco_dados:
                    print("CPF não está cadastrado.")
                else:
                    if len(banco_dados[cpf_limpo]) > 0:
                        print("Não é possível remover o CPF. Existem MACs vinculados.")
                    else:
                        del banco_dados[cpf_limpo]
                        print(f"CPF {cpf_limpo} removido com sucesso.")

        if opcao == 5:
            print("\nVocê escolheu: 5 - Listar os CPFs cadastrados")

            if len(banco_dados) == 0:
                print("Nenhum CPF cadastrado no sistema.")
            else:
                print("CPFs cadastrados:")
                for cpf in banco_dados:
                    print(f"cpf - {cpf}")

        if opcao == 6:
            print("\nVocê escolheu: 6 - Listar os MAC addresses vinculados a um CPF")

            cpf_input = input("Digite o CPF para listar os MACs vinculados: ").strip()

            if cpf_valido(cpf_input) == False:
                print("CPF inválido!")
            else:
                cpf_limpo = cpf_input.replace(".", "").replace("-", "")

                if cpf_limpo not in banco_dados:
                    print("CPF não está cadastrado.")
                else:
                    macs = banco_dados[cpf_limpo]
                    if len(macs) == 0:
                        print("Nenhum MAC address vinculado a esse CPF.")
                    else:
                        print(f"MAC addresses vinculados ao CPF {cpf_input}:")
                        for mac in macs:
                            print(f"- {mac}")

        if opcao == 7:
            print("\nVocê escolheu: 7 - Salvar o banco de dados em um arquivo")

            import json

            nome_arquivo = input("Digite o nome do arquivo para salvar (ex: dados.json): ").strip()

            try:
                with open(nome_arquivo, 'w') as arquivo:
                    json.dump(banco_dados, arquivo) # # Salva o dicionário 'banco_dados' no arquivo aberto, convertendo os dados para o formato JSON
                print(f"Banco de dados salvo com sucesso em '{nome_arquivo}'!")
            except Exception as e:
                print(f"Erro ao salvar o arquivo: {e}")

        if opcao == 8:
            print("\nVocê escolheu: 8 - Ler o banco de dados de um arquivo")

            import json

            nome_arquivo = input("Digite o nome do arquivo para ler (ex: dados.json): ").strip()

            try:
                with open(nome_arquivo, 'r') as arquivo:
                    banco_dados = json.load(arquivo)
                print(f"Banco de dados carregado com sucesso de '{nome_arquivo}'!")
                print(banco_dados)
            except FileNotFoundError:
                print("Arquivo não encontrado.")
            except json.JSONDecodeError:
                print("Erro: o arquivo não está em formato JSON válido.")
            except Exception as e:
                print(f"Erro ao ler o arquivo: {e}")

        elif opcao == 9:
            print("\nEncerrando o programa...")
            break
        else:
            print("\nExecução finalizada.")
    else:
        print("\nOpção inválida. Digite um número válido.")
