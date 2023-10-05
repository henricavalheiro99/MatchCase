num = int(input("Digite um número de 1 a 3: "))
#if num == 1:
 #   print("Amarelo")
#elif num == 2:
#   print("Azul")
#elif num == 3:
#    print("Verde")
#else:
#    print("Sem cor")

match num:
    case 1:
        print("Amarelo")
    case 2:
        print("Azul")
    case 3:
        print("Verde")
    case _:
        print("Sem cor")