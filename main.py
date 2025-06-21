#Projeto final Matemática Financeira
#Aluno: Emanoel Borges
#Professora: Mara

def jurosSimples(vp, i, n):
    j = vp * i * n
    return j

def valorFuturo(vp, i, n):
    vf = vp * (1 + i * n)
    return vf

def main():
    
    while True:
    
        print("--- Calculadora Financeira ---")
        print("Escolha uma opcao:")
        print("1 - Calcular juros simples ")
        print("0 - Sair ")

        opcao = int(input("\nDigite a opcao (1 a ?): "))

        if opcao == 1:
            print("Vamos calcular o juros simples!")
            vp = float(input("Digite o valor presente R$ "))
            i = float(input("Digite a taxa: "))
            n = float(input("Digite o tempo: "))
            juros = jurosSimples(vp, i, n)
            print(f"O valor do juros simples é: R$ {juros:.2f}")
            print(f"O valor futuro é: R$ {valorFuturo(vp, i, n):.2f}") 

        elif opcao == 0:
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.\n")

main()
