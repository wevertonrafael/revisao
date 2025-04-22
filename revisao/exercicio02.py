resposta = "S"
while resposta =="S":
    number = int(input("Digite um número: "))
    if number % 2==0 and number <0:
        print(f"O number é PAR e NEGATIVO: ")

    elif number % 2==0 and number >0:
        print((f"O number é PAR e POSITIVO: "))


    elif number % 3==0 and number >0:
        print(f"O number é: {number} POSITIVO: ")
    else:
        print(f"O number é: {number} NEGATIVO: ")
    resposta =(input("Deseja verificar novo número?: "))