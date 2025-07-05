#Projeto final Matemática Financeira
#Aluno: Emanoel Borges
#Professora: Mara
def conversao(n, tipo_taxa, tipo_tempo):
    if tipo_taxa == tipo_tempo:
        return n
    else:
        if tipo_taxa == "ano":
            if tipo_tempo == "mes":
                 n_convertido = n / 12
                 return n_convertido
            elif tipo_tempo == "dia":
                n_convertido = n / 360
                return n_convertido
        elif tipo_taxa == "mes":
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
            elif tipo_tempo == "mes":
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

def descontoComercial(vf, desconto, tempo):
    return desconto / (vf * tempo)

def taxaEfetiva(vp, desconto, tempo):
    return desconto / (vp * tempo)

def main():
    
    while True:
    
        print("\n=== Calculadora Financeira – Capitalização Simples ===")
        print("1 - Calcular Juros (J)")
        print("2 - Calcular Capital (VP)")
        print("3 - Calcular Montante (VF)")
        print("4 - Calcular Taxa (i)")
        print("5 - Calcular Tempo (n)")
        print("6 - Calcular Taxa de Desconto Comercial (iC)")
        print("7 - Calcular Taxa Efetiva (i)")
        print("0 - Sair")

        opcao = int(input("\nDigite a opcao (0 a 7): "))

        if opcao == 1:
            print("Vamos calcular os Juros!")
            vp = float(input("Digite o valor presente (VP) R$: "))
            i = float(input("Digite a taxa (%): ")) / 100
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower()
            n = float(input("Digite o tempo: "))
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower()# O Lower converte todas as letras de uma string em minúscula.
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            j = jurosSimples(vp, i, n_convertido)
            print(f"O valor dos Juros é: R$ {round(j, 2)}")#round é usado para arredondar as casas decimais.Também podemos fazer sem usar o round, um exemplo abaixo.

        elif opcao == 2:
            print("Vamos calcular o Valor Presente (Capital)!")
            vf = float(input("Digite o valor futuro (VF) R$: "))
            i = float(input("Digite a taxa (%): ")) / 100
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower()
            n = float(input("Digite o tempo: "))
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower()
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            vp = valorPresente(vf, i, n_convertido)
            print(f"O valor do Capital (VP) é: R$ {round(vp, 2)}")

        elif opcao == 3:
            print("Vamos calcular o Valor Futuro (Montante)!")
            vp = float(input("Digite o valor presente (VP) R$: "))
            i = float(input("Digite a taxa (%): ")) / 100
            tipo_taxa = input("Digite o tipo da taxa (dia/mês/ano): ").lower()
            n = float(input("Digite o tempo: "))
            tipo_tempo = input("Digite o tipo do tempo (dia/mês/ano): ").lower()
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            vf = valorFuturo(vp, i, n_convertido)
            print(f"O valor do Montante (VF) é: R$ {round(vf, 2)}")

        elif opcao == 4:
            print("Vamos calcular a Taxa!")
            vp = float(input("Digite o valor presente R$ "))
            n = float(input("Digite o tempo: "))
            vf = float(input("Digite o valor futuro R$ "))
            i = taxa(vp, n, vf) * 100
            print(f"O valor da taxa é: {round(i,2)} %")

        elif opcao == 5:
            print("Vamos calcular a Tempo (n)!")
            vp = float(input("Digite o valor presente R$ "))
            i = float(input("Digite a taxa em (%): ")) / 100
            vf = float(input("Digite o valor futuro R$ "))
            n = tempo(vf, vp, i)
            print(f"O tempo necessário é:",n,"períodos")

        elif opcao == 6:
            print("Vamos calcular a taxa de desconto comercial!")
            vf = float(input("Digite o valor futuro R$ "))
            d = float(input("Digite o valor do desconto comercial R$ "))
            n = float(input("Digite o tempo: "))
            print("Taxa de desconto comercial é:",descontoComercial(vf, d, n) * 100, "%")

        elif opcao == 7:
            print("Vamos calcular a taxa efetiva!")
            vp = float(input("Digite o valor presente R$ "))
            d = float(input("Digite o valor do desconto R$ "))
            n = float(input("Digite o tempo: "))
            print("Taxa efetiva é:",taxaEfetiva(vp, d, n) * 100, "%")

        elif opcao == 0:
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.\n")

main()
