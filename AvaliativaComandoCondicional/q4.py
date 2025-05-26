mes_inicial = int(input("Digite o mês inicial: "))

# Verificador mês inicial (O mês deve ser maior ou igual a 1 e menor ou igual a 12)
if mes_inicial < 1:
    print("Mês inicial inválido")
else:
    if mes_inicial > 12:
        print("Mês inicial inválido")
    else:
        dia_inicial = int(input("Digite o dia inicial: "))

        # Verificador limite de dias do mês inicial
        if mes_inicial == 2:  # Fevereiro
            max_dia_inicial = 28
        else:
            if mes_inicial == 4:  # Abril
                max_dia_inicial = 30
            else:
                if mes_inicial == 6:  # Junho
                    max_dia_inicial = 30
                else:
                    if mes_inicial == 9:  # Setembro
                        max_dia_inicial = 30
                    else:
                        if mes_inicial == 11:  # Novembro
                            max_dia_inicial = 30
                        else:
                            max_dia_inicial = 31  # Restante dos meses têm 31 dias

        # Verificador dia inicial (O dia deve ser maior ou igual a 1 e menor ou igual ao máximo do mês)
        if dia_inicial < 1:
            print("Dia inicial inválido")
        else:
            if dia_inicial > max_dia_inicial:
                print("Dia inicial inválido")
            else:
                # Solicita o mês final
                mes_final = int(input("Digite o mês final: "))

                # Verificador mês final
                if mes_final < 1:
                    print("Mês final inválido")
                else:
                    if mes_final > 12:
                        print("Mês final inválido")
                    else:
                        # Solicita o dia final
                        dia_final = int(input("Digite o dia final: "))

                        # Verificador limite de dias do mês final
                        if mes_final == 2:  # Fevereiro
                            max_dia_final = 28
                        else:
                            if mes_final == 4:  # Abril
                                max_dia_final = 30
                            else:
                                if mes_final == 6:  # Junho
                                    max_dia_final = 30
                                else:
                                    if mes_final == 9:  # Setembro
                                        max_dia_final = 30
                                    else:
                                        if mes_final == 11:  # Novembro
                                            max_dia_final = 30
                                        else:
                                            max_dia_final = 31  # Demais meses

                        # Verificador dia final
                        if dia_final < 1:
                            print("Dia final inválido")
                        else:
                            if dia_final > max_dia_final:
                                print("Dia final inválido")
                            else:
                                # Cálculo dos dias acumulados ate a data inicial
                                if mes_inicial == 1: # Janeiro
                                    dias_ate_inicial = dia_inicial
                                else:
                                    if mes_inicial == 2: # fevereiro
                                        dias_ate_inicial = 31 + dia_inicial
                                    else:
                                        if mes_inicial == 3: # Março
                                            dias_ate_inicial = 31 + 28 + dia_inicial
                                        else:
                                            if mes_inicial == 4: # Abril
                                                dias_ate_inicial = 31 + 28 + 31 + dia_inicial
                                            else:
                                                if mes_inicial == 5: # Maio
                                                    dias_ate_inicial = 31 + 28 + 31 + 30 + dia_inicial
                                                else:
                                                    if mes_inicial == 6: # Junho
                                                        dias_ate_inicial = 31 + 28 + 31 + 30 + 31 + dia_inicial
                                                    else:
                                                        if mes_inicial == 7: # Julho
                                                            dias_ate_inicial = 31 + 28 + 31 + 30 + 31 + 30 + dia_inicial
                                                        else:
                                                            if mes_inicial == 8: # agoto
                                                                dias_ate_inicial = 31 + 28 + 31 + 30 + 31 + 30 + 31 + dia_inicial
                                                            else:
                                                                if mes_inicial == 9: # setembro
                                                                    dias_ate_inicial = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + dia_inicial
                                                                else:
                                                                    if mes_inicial == 10: # Outubro
                                                                        dias_ate_inicial = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + dia_inicial
                                                                    else:
                                                                        if mes_inicial == 11: # Novembro
                                                                            dias_ate_inicial = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + dia_inicial
                                                                        else:  # Dezembro
                                                                            dias_ate_inicial = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + dia_inicial

                                # Cálculo dos dias acumulados ate a data final
                                if mes_final == 1:
                                    dias_ate_final = dia_final
                                else:
                                    if mes_final == 2:
                                        dias_ate_final = 31 + dia_final
                                    else:
                                        if mes_final == 3:
                                            dias_ate_final = 31 + 28 + dia_final
                                        else:
                                            if mes_final == 4:
                                                dias_ate_final = 31 + 28 + 31 + dia_final
                                            else:
                                                if mes_final == 5:
                                                    dias_ate_final = 31 + 28 + 31 + 30 + dia_final
                                                else:
                                                    if mes_final == 6:
                                                        dias_ate_final = 31 + 28 + 31 + 30 + 31 + dia_final
                                                    else:
                                                        if mes_final == 7:
                                                            dias_ate_final = 31 + 28 + 31 + 30 + 31 + 30 + dia_final
                                                        else:
                                                            if mes_final == 8:
                                                                dias_ate_final = 31 + 28 + 31 + 30 + 31 + 30 + 31 + dia_final
                                                            else:
                                                                if mes_final == 9:
                                                                    dias_ate_final = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + dia_final
                                                                else:
                                                                    if mes_final == 10:
                                                                        dias_ate_final = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + dia_final
                                                                    else:
                                                                        if mes_final == 11:
                                                                            dias_ate_final = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + dia_final
                                                                        else:  # Dezembro
                                                                            dias_ate_final = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + dia_final

                                # Calcula os dias decorridos
                                dias_decorridos = dias_ate_final - dias_ate_inicial

                                # Verificador data final é posterior à data inicial
                                if dias_decorridos < 0:
                                    print("A data final deve ser posterior à data inicial")
                                else:
                                    print("Número de dias decorridos:", dias_decorridos)
