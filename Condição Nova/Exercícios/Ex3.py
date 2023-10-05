dia = str(input("Digite um dia da semana: "))
def IdentificaDia (a):
    match a:
        case ("segunda" | "terça" | "quarta" | "quinta" | "sexta"):
            if a == "segunda":
                print("Tristeza")
            elif a == "terça":
                print("Aula do Hugoooooo")
            elif a == "quarta":
                print("Meio caminho andado")
            elif a == "quinta":
                print("Aula do Bru Bru")
            elif a == "sexta":
                print("Aula do Iguinho")
        case ("sábado" | "domingo"):
            if a == "sábado":
                print("Dia de maldade")
            elif a == "domingo":
                print("Dia do foda-se")

IdentificaDia(dia)
