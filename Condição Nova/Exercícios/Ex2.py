cor = str(input("Digite uma cor: "))

def IdentificaCor (a):
    match a:
        case "vermelho":
            print("A cor é vermelho")
        case "azul":
            print("A cor é azul")
        case "verde":
            print("A cor é verde")
        case _:
            print("Cor desconhecida")

IdentificaCor(cor)