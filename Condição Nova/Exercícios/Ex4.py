animal = str(input("Digite um animal: "))

def IdentificaAnimal (a):
    match a:
        case "vaca":
            print("O animal é vaca")
        case "galinha":
            print("O animal é galinha")
        case "ovelha":
            print("O animal é ovelha")
        case _:
            print("Animal desconhecido")

IdentificaAnimal(animal)