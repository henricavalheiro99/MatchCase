login = str(input("Digite o login: "))
senha = str(input("Digite a senha: "))

def IdentificaUser (a, b):
    match (a, b):
        case "admin", "admin_pass":
            print("Válido")
        case "user", "user_pass":
            print("Válido")
        case "guest", "_":
            print("Válido")
        case _:
            print("Bloqueado")

IdentificaUser(login, senha)