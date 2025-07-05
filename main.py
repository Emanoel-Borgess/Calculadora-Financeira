#Projeto final Matemática Financeira
#Aluno: Emanoel Borges
#Professora: Mara
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
            print("Vamos calcular o valor presente (Capital)!")
            vf = float(input("Digite o valor final R$ "))
            juros = float(input("Digite o valor do juros R$ "))
            i = float(input("Digite a taxa: ")) / 100
            tipo_taxa = str(input("Digite o tipo da taxa (dia/mês/ano): ")).lower()# O Lower converte todas as letras de uma string em minúscula.
            n = float(input("Digite o tempo: "))
            tipo_tempo = str(input("Digite o tipo do tempo (dia/mês/ano): ")).lower()
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            capital = valorPresente(vf, i, n_convertido)
            print(f"O valor do Capital é: R$",round(capital,2))#round é usado para arredondar as casas decimais.Também podemos fazer sem usar o round, um exemplo abaixo.

        elif opcao == 2:
            print("Vamos calcular o valor futuro (Montante)!")
            vf = float(input("Digite o valor final R$ "))
            juros = float(input("Digite o valor do juros R$ "))
            i = float(input("Digite a taxa: ")) / 100
            tipo_taxa = str(input("Digite o tipo da taxa (dia/mês/ano): ")).lower()
            n = float(input("Digite o tempo: "))
            tipo_tempo = str(input("Digite o tipo do tempo (dia/mês/ano): ")).lower()
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            montante = valorFuturo(vp, i, n_convertido)
            print(f"O valor do Montante é: R$",round(montante,2))

        elif opcao == 3:
            print("Vamos calcular o juros simples!")
            vp = float(input("Digite o valor presente R$ "))
            i = float(input("Digite a taxa: ")) / 100
            tipo_taxa = str(input("Digite o tipo da taxa (dia/mês/ano): ")).lower()
            n = float(input("Digite o tempo: "))
            tipo_tempo = str(input("Digite o tipo do tempo (dia/mês/ano): ")).lower()
            n_convertido = conversao(n, tipo_taxa, tipo_tempo)
            juros_simples = jurosSimples(vp, i, n_convertido)
            print(f"O valor do juros simples é: R$",round(juros_simples,2))

        elif opcao == 4:
            print("Vamos calcular a Taxa!")
            vp = float(input("Digite o valor presente R$ "))
            n = float(input("Digite o tempo: "))
            vf = float(input("Digite o valor futuro R$ "))
            i = taxa(vp, n, vf) * 100
            print(f"O valor da taxa é: R$",i,"%")

        elif opcao == 5:
            print("Vamos calcular a Tempo!")
            vp = float(input("Digite o valor presente R$ "))
            i = float(input("Digite a taxa em (%): "))
            vf = float(input("Digite o valor futuro R$ "))
            n = tempo(vp, i, vf) / 100
            print(f"O valor da taxa é: R$",n)

        elif opcao == 6:
            vf = float(input("Digite o valor futuro R$ "))
            d = float(input("Digite o valor do desconto comercial R$ "))
            n = float(input("Digite o tempo:"))
            print("Taxa de desconto comercial é:",descontoComercial(vf, d, n) * 100, "%")

        elif opcao == 7:
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
