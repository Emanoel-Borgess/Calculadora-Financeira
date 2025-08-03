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
    
def valorPresente(vf, i, n):
    vp = vf / (1 + (i * n))
    return vp

def valorFuturo(vp, i, n):
    vf = vp * (1 + i * n)
    return vf

def jurosSimples(vp, i, n):
    j = vp * i * n
    return j

def taxa(vp, n, vf):
    i = ((vf / vp) - 1) / n
    return i

def tempo(vf, vp, i):
    n = ((vf / vp) - 1) / i
    return n

def taxaDescontoComercial(i, n):
    return i / (1 + (i * n))

def taxaDeJurosEfetiva(ic, n):
    return ic / (1 - ic * n)

def jurosComposto(vp, i, n):
    return vp * ((1 + i) ** n - 1)

def capitalComposto(vf, i, n):
    return vf / ((1 + i) ** n)

def montanteComposto(vp, i, n):
    return vp * ((1 + i) ** n)

def taxaComposta(vp, vf, n):
    return (vf / vp) ** (1 / n) - 1

def tempoComposto(vf, vp, i):
    return math.log(vf / vp) / math.log(1 + i)

def main():
    
    while True:
    
        print("\n=== Calculadora Financeira ===")
        print("\n=== Calculadora Financeira - Parte de capitalização simples ===")
        print("1 - Calcular Juros (J)")
        print("2 - Calcular Capital (VP)")
        print("3 - Calcular Montante (VF)")
        print("4 - Calcular Taxa (i)")
        print("5 - Calcular Tempo (n)")
        print("6 - Calcular Taxa de Desconto Comercial (iC)")
        print("7 - Calcular Taxa Efetiva (i)")
        print("\n=== Calculadora Financeira - Parte de capitalização composta ===")
        print("8 - Calcular Juros Composto (J)")
        print("9 - Calcular Capital Composto (VP)")
        print("10 - Calcular Montante Composto (VF)")
        print("11 - Calcular Taxa Composta (i)")
        print("12 - Calculando Tempo Composto (n)")
        print("0 - Sair")

        opcao = int(input("\nDigite a opcao (0 a 12): "))

        if opcao == 1:
            print("Vamos calcular os Juros!")
            vp = float(input("Digite o valor presente (VP) R$: "))
            i = float(input("Digite a taxa (%): ")) / 100
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            n = float(input("Digite o tempo: "))
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")# O Lower converte todas as letras de uma string em minúscula.
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            if n_convertido is None:
                print("Erro: tipos de taxa e tempo incompatíveis. Tente novamente.")
                continue
            j = jurosSimples(vp, i, n_convertido)
            print(f"O valor dos Juros é: R$ {round(j, 2)}")#round é usado para arredondar as casas decimais.Também podemos fazer sem usar o round, um exemplo abaixo.

        elif opcao == 2:
            print("Vamos calcular o Valor Presente (Capital)!")
            vf = float(input("Digite o valor futuro (VF) R$: "))
            i = float(input("Digite a taxa (%): ")) / 100
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            n = float(input("Digite o tempo: "))
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            if n_convertido is None:
                print("Erro: tipos de taxa e tempo incompatíveis. Tente novamente.")
                continue
            vp = valorPresente(vf, i, n_convertido)
            print(f"O valor do Capital (VP) é: R$ {round(vp, 2)}")

        elif opcao == 3:
            print("Vamos calcular o Valor Futuro (Montante)!")
            vp = float(input("Digite o valor presente (VP) R$: "))
            i = float(input("Digite a taxa (%): ")) / 100
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            n = float(input("Digite o tempo: "))
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            if n_convertido is None:
                print("Erro: tipos de taxa e tempo incompatíveis. Tente novamente.")
                continue
            vf = valorFuturo(vp, i, n_convertido)
            print(f"O valor do Montante (VF) é: R$ {round(vf, 2)}")

        elif opcao == 4:
            print("Vamos calcular a Taxa!")
            vp = float(input("Digite o valor presente (VP) R$: "))
            vf = float(input("Digite o valor futuro (VF) R$: "))
            n = float(input("Digite o tempo: "))
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            if n_convertido is None:
                print("Erro: tipos de taxa e tempo incompatíveis. Tente novamente.")
                continue
            i = taxa(vp, n_convertido, vf) * 100
            print(f"O valor da taxa é: {round(i, 2)}%")

        elif opcao == 5:
            print("Vamos calcular o Tempo (n)!")
            vp = float(input("Digite o valor presente (VP) R$: "))
            vf = float(input("Digite o valor futuro (VF) R$: "))
            i = float(input("Digite a taxa (%): ")) / 100
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")
            # Aqui a conversão é do tempo que será calculado, então invertemos a lógica para preservar unidade da taxa
            n = tempo(vf, vp, i)
            print(f"O tempo necessário é: {round(n, 2)} períodos na unidade da taxa ({tipo_taxa})")

        elif opcao == 6:
            print("Vamos calcular a Taxa de Desconto Comercial!")
            i = float(input("Digite a taxa: "))
            n = float(input("Digite o tempo: "))
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            if n_convertido is None:
                print("Erro: tipos de taxa e tempo incompatíveis. Tente novamente.")
                continue
            ic = taxaDescontoComercial(i, n_convertido) * 100
            print(f"Taxa de desconto comercial: {round(ic, 2)}%")

        elif opcao == 7:
            print("Vamos calcular a Taxa de Juros Efetiva!")
            ic = float(input("Digite a taxa de desconto "))
            n = float(input("Digite o tempo: "))
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            if n_convertido is None:
                print("Erro: tipos de taxa e tempo incompatíveis. Tente novamente.")
                continue
            i = taxaDeJurosEfetiva(ic, n_convertido) * 100
            print(f"Taxa efetiva: {round(i, 2)}%")

        elif opcao == 8:
            print("Vamos calcular o juros composto")
            vp = float(input("Digite o valor presente: "))
            i = float(input("Digite a taxa: ")) / 100
            n = float(input("Digite o tempo: "))
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            if n_convertido is None:
                print("Erro: tipos de taxa e tempo incompatíveis. Tente novamente.")
                continue
            j = jurosComposto(vp, i, n_convertido)
            print(f"O juros é de: R$ {round(j, 2)}")

        elif opcao == 9:
            print("Vamos calcular o capital composto")
            vf = float(input("Digite o valor futuro: "))
            i = float(input("Digite a taxa: ")) / 100
            n = float(input("Digite o tempo: "))
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            if n_convertido is None:
                print("Erro: tipos de taxa e tempo incompatíveis. Tente novamente.")
                continue
            vp = capitalComposto(vf, i, n_convertido)
            print(f"O capital é de: R$ {round(vp, 2)}")
        
        elif opcao == 10:
            print("Vamos calcular o montante composto")
            vp = float(input("Digite o valor presente: "))
            i = float(input("Digite a taxa: ")) / 100
            n = float(input("Digite o tempo: "))
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            if n_convertido is None:
                print("Erro: tipos de taxa e tempo incompatíveis. Tente novamente.")
                continue
            vf = montanteComposto(vp, i, n_convertido)
            print(f"O montante é de: R$ {round(vf, 2)}")

        elif opcao == 11:
            print("Vamos calcular a taxa composta")
            vp = float(input("Digite o valor presente: "))
            vf = float(input("Digite o valor futuro: "))
            n = float(input("Digite o tempo: "))
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            if n_convertido is None:
                print("Erro: tipos de taxa e tempo incompatíveis. Tente novamente.")
                continue
            i = taxaComposta(vp, vf, n_convertido) * 100
            print(f"A taxa é de: {round(i, 2)}%")

        elif opcao == 12:
            print("Vamos calcular o tempo composto")
            vp = float(input("Digite o valor presente: "))
            vf = float(input("Digite o valor futuro: "))
            i = float(input("Digite a taxa: ")) / 100
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower().replace("mes", "mês")
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower().replace("mes", "mês")
            n = tempoComposto(vf, vp, i)
            print(f"O tempo necessário é: {round(n, 2)} períodos na unidade da taxa ({tipo_taxa})")

        elif opcao == 0:
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.\n")

main()
