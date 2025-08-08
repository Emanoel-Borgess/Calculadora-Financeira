#Projeto final Matemática Financeira
#Aluno: Emanoel Borges
#Professora: Mara

import math

def conversao(n, tipo_taxa, tipo_tempo):
    if tipo_taxa == tipo_tempo:
        return n
    else:
        if tipo_taxa == "ano":
            if tipo_tempo == "mês":
                 n_convertido = n / 12
                 return n_convertido
            elif tipo_tempo == "dia":
                n_convertido = n / 360
                return n_convertido
        elif tipo_taxa == "mês":
            if tipo_tempo == "ano":
                n_convertido = n * 12
                return n_convertido
            elif tipo_tempo == "dia":
                n_convertido = n / 30
                return n_convertido
        elif tipo_taxa == "dia":
            if tipo_tempo == "ano":
                n_convertido = n * 360
                return n_convertido
            elif tipo_tempo == "mês":
                n_convertido = n * 30
                return n_convertido
        return None #None significa um retorno sem valor
    
def valor_presente_simples(vf, i, n):
    vp = vf / (1 + (i * n))
    return vp

def valor_futuro_simples(vp, i, n):
    vf = vp * (1 + i * n)
    return vf

def juros_simples(vp, i, n):
    j = vp * i * n
    return j

def taxa_simples(vp, n, vf):
    i = ((vf / vp) - 1) / n
    return i

def tempo_simples(vf, vp, i):
    n = ((vf / vp) - 1) / i
    return n

def taxa_desconto_comercial_simples(i, n):
    return i / (1 + (i * n))

def taxa_juros_efetiva_simples(ic, n):
    return ic / (1 - ic * n)

def juros_composto(vp, i, n):
    return vp * ((1 + i) ** n - 1)

def valor_presente_composto(vf, i, n):
    return vf / ((1 + i) ** n)

def valor_futuro_composto(vp, i, n):
    return vp * ((1 + i) ** n)

def taxa_composta(vp, vf, n):
    return (vf / vp) ** (1 / n) - 1

def tempo_composto(vf, vp, i):
    return math.log(vf / vp) / math.log(1 + i)

def nominal_para_efetiva(ik, k):
    return ik / k

def efetiva_para_nominal(i, k):
    return i * k

def taxa_equivalente(i_origem, n_origem, n_destino):
    return (1 + i_origem) ** (n_origem / n_destino) - 1


def main():
    
    while True:
    
        print("\n=== Calculadora Financeira ===")

        print("\n=== Calculadora Financeira - Parte de capitalização simples ===")

        print("1 - Calcular Juros Simples (J)")
        print("2 - Calcular Valor Presente (Capital) (VP)")
        print("3 - Calcular Valor Futuro (Montante) (VF)")
        print("4 - Calcular Taxa (i)")
        print("5 - Calcular Tempo (n)")
        print("6 - Calcular Taxa de Desconto Comercial (iC)")
        print("7 - Calcular Taxa Efetiva (i)")

        print("\n=== Calculadora Financeira - Parte de capitalização composta ===")

        print("8 - Calcular Juros Composto (J)")
        print("9 - Calcular Valor Presente (Capital) (VP)")
        print("10 - Calcular Valor Futuro (Montante) (VF)")
        print("11 - Calcular Taxa (i)")
        print("12 - Calculando Tempo (n)")
        print("13 - Converter taxa nominal para efetiva")
        print("14 - Converter taxa efetiva para nominal")
        print("15 - Converter taxas efetivas equivalentes entre períodos")
        print("\n0 - Sair")

        opcao = int(input("\nDigite a opcao (0 a 15): "))

        if opcao == 1:
            print("\nVamos calcular o Juros Simples\n")
            vp = float(input("Digite o valor presente R$: "))
            i = float(input("Digite a taxa: ")) / 100
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            n = float(input("Digite o tempo: "))
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")# O Lower converte todas as letras de uma string em minúscula.
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            if n_convertido is None:
                print("Erro: tipos de taxa e tempo incompatíveis. Tente novamente.")
                continue
            j = juros_simples(vp, i, n_convertido)
            print(f"O valor dos Juros é: R$ {round(j, 2)}")#round é usado para arredondar as casas decimais.Também podemos fazer sem usar o round, um exemplo abaixo.

        elif opcao == 2:
            print("Vamos calcular o Valor Presente (Capital)")
            vf = float(input("Digite o valor futuro R$: "))
            i = float(input("Digite a taxa: ")) / 100
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            n = float(input("Digite o tempo: "))
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            if n_convertido is None:
                print("Erro: tipos de taxa e tempo incompatíveis. Tente novamente.")
                continue
            vp = valor_presente_simples(vf, i, n_convertido)
            print(f"O valor do Capital é: R$ {round(vp, 2)}")

        elif opcao == 3:
            print("Vamos calcular o Valor Futuro (Montante)")
            vp = float(input("Digite o valor presente R$: "))
            i = float(input("Digite a taxa: ")) / 100
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            n = float(input("Digite o tempo: "))
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            if n_convertido is None:
                print("Erro: tipos de taxa e tempo incompatíveis. Tente novamente.")
                continue
            vf = valor_futuro_simples(vp, i, n_convertido)
            print(f"O valor do Montante é: R$ {round(vf, 2)}")

        elif opcao == 4:
            print("Vamos calcular a Taxa")
            vp = float(input("Digite o valor presente R$: "))
            vf = float(input("Digite o valor futuro R$: "))
            n = float(input("Digite o tempo: "))
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            if n_convertido is None:
                print("Erro: tipos de taxa e tempo incompatíveis. Tente novamente.")
                continue
            i = taxa_simples(vp, n_convertido, vf) * 100
            print(f"O valor da taxa é: {round(i, 2)}% ao ({tipo_taxa})")

        elif opcao == 5:
            print("Vamos calcular o Tempo")
            vp = float(input("Digite o valor presente R$: "))
            vf = float(input("Digite o valor futuro R$: "))
            i = float(input("Digite a taxa: ")) / 100
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")
            # Aqui a conversão é do tempo que será calculado, então invertemos a lógica para preservar unidade da taxa
            n = tempo_simples(vf, vp, i)
            print(f"O tempo necessário é de: {round(n, 2)} períodos na unidade da taxa ({tipo_taxa})")

        elif opcao == 6:
            print("Vamos calcular a Taxa de Desconto Comercial")
            i = float(input("Digite a taxa: ")) / 100
            n = float(input("Digite o tempo: "))
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            if n_convertido is None:
                print("Erro: tipos de taxa e tempo incompatíveis. Tente novamente.")
                continue
            ic = taxa_desconto_comercial_simples(i, n_convertido) * 100
            print(f"Taxa de desconto comercial é de: {round(ic, 2)}%")

        elif opcao == 7:
            print("Vamos calcular a Taxa de Juros Efetiva")
            ic = float(input("Digite a taxa de desconto ")) / 100
            n = float(input("Digite o tempo: "))
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            if n_convertido is None:
                print("Erro: tipos de taxa e tempo incompatíveis. Tente novamente.")
                continue
            i = taxa_juros_efetiva_simples(ic, n_convertido) * 100
            print(f"A Taxa efetiva é de: {round(i, 2)}%")

        elif opcao == 8:
            print("Vamos calcular o Juros Composto")
            vp = float(input("Digite o valor presente: "))
            i = float(input("Digite a taxa: ")) / 100
            n = float(input("Digite o tempo: "))
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            if n_convertido is None:
                print("Erro: tipos de taxa e tempo incompatíveis. Tente novamente.")
                continue
            j = juros_composto(vp, i, n_convertido)
            print(f"O juros é de: R$ {round(j, 2)}")

        elif opcao == 9:
            print("Vamos calcular o Valor Presente (Capital)")
            vf = float(input("Digite o valor futuro: "))
            i = float(input("Digite a taxa: ")) / 100
            n = float(input("Digite o tempo: "))
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            if n_convertido is None:
                print("Erro: tipos de taxa e tempo incompatíveis. Tente novamente.")
                continue
            vp = valor_presente_composto(vf, i, n_convertido)
            print(f"O capital é de: R$ {round(vp, 2)}")
        
        elif opcao == 10:
            print("Vamos calcular o VCalor Futuro (Montante)")
            vp = float(input("Digite o valor presente: "))
            i = float(input("Digite a taxa: ")) / 100
            n = float(input("Digite o tempo: "))
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            if n_convertido is None:
                print("Erro: tipos de taxa e tempo incompatíveis. Tente novamente.")
                continue
            vf = valor_futuro_composto(vp, i, n_convertido)
            print(f"O montante é de: R$ {round(vf, 2)}")

        elif opcao == 11:
            print("Vamos calcular a Taxa")
            vp = float(input("Digite o valor presente: "))
            vf = float(input("Digite o valor futuro: "))
            n = float(input("Digite o tempo: "))
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            if n_convertido is None:
                print("Erro: tipos de taxa e tempo incompatíveis. Tente novamente.")
                continue
            i = taxa_composta(vp, vf, n_convertido) * 100
            print(f"A taxa é de: {round(i, 2)}% ao ({tipo_taxa})")

        elif opcao == 12:
            print("Vamos calcular o Tempo")
            vp = float(input("Digite o valor presente: "))
            vf = float(input("Digite o valor futuro: "))
            i = float(input("Digite a taxa: ")) / 100
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")
            n = tempo_composto(vf, vp, i)
            print(f"O tempo necessário é: {round(n, 2)} períodos na unidade da taxa ({tipo_taxa})")

        elif opcao == 13:
            print("Conversão da Taxa Nominal para Efetiva Proporcional")
            print("Para os períodos digite as seguintes opções:")
            print("12 para mensal")
            print("4 para trimestral")
            print("2 para semestral")
            print("1 para anual")
            print("360 para diária (ano comercial)\n")

            ik = float(input("Digite a taxa nominal: ")) / 100
            k = int(input("Digite o número de períodos: "))
            i = nominal_para_efetiva(ik, k) * 100
            print(f"A taxa efetiva proporcional é: {round(i, 2)}%")

        elif opcao == 14:
            print("Conversão da Taxa Efetiva Proporcional para Nominal")
            print("Para os períodos digite as seguintes opções:")
            print("12 para mensal")
            print("4 para trimestral")
            print("2 para semestral")
            print("1 para anual")
            print("360 para diária (ano comercial)\n")

            i = float(input("Digite a taxa efetiva proporcional: ")) / 100
            k = int(input("Digite o número de períodos: "))
            ik = efetiva_para_nominal(i, k) * 100
            print(f"A taxa nominal é: {round(ik, 2)}%")

        elif opcao == 15:
            print("=== Conversão entre taxas efetivas equivalentes ===")
            print("Sempre digite as taxas em porcentagem, como 2 para 2%")
            print("Para os períodos digite as seguintes opções:")
            print("12 para mensal")
            print("4 para trimestral")
            print("2 para semestral")
            print("1 para anual")
            print("360 para diária (ano comercial)\n")
            
            print("Você deseja converter de:")
            print("1 - Tempo menor para maior (ex: mensal → anual)")
            print("2 - Tempo maior para menor (ex: anual → mensal)")

            tipo_conversao = input("Escolha a opção (1 ou 2): ")

            if tipo_conversao == "1":
                print("\nTempo menor para maior")
                i = float(input("Digite a taxa efetiva no período menor: ")) / 100
                n_menor = float(input("Número de períodos da taxa informada: "))
                n_maior = float(input("Número de períodos desejado: "))

                i_eq = taxa_equivalente(i, n_menor, n_maior) * 100
                print(f"Taxa equivalente no período maior: {round(i_eq, 2)}%")

            elif tipo_conversao == "2":
                print("\nTempo maior para menor")
                i = float(input("Digite a taxa efetiva no período maior: ")) / 100
                n_maior = float(input("Número de períodos da taxa informada: "))
                n_menor = float(input("Número de períodos desejado: "))

                i_eq = taxa_equivalente(i, n_maior, n_menor) * 100
                print(f"Taxa equivalente no período menor: {round(i_eq, 2)}%")

            else:
                print("Opção inválida. Escolha 1 ou 2.")

        elif opcao == 0:
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.\n")

main()
