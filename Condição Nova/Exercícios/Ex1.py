num = int(input("Digite um número de 1 a 3: "))
def RetornaValor (a):
    match a:
        case 1:
            print("O número é: 1")
        case 2:
            print("O número é 2")
        case 3:
            print("O número é 3")
        case _:
            print("Inválido")

RetornaValor(num)