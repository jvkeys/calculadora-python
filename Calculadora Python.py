#Calculadora
# Cria o loop do programa
while True:

    # Recebe os dois números do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Exibir o menu de operações
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    opcao = input("Digite o número da operação: ")

    # Realiza a operação escolhida
    if opcao == "1":
        print("Resultado:", num1 + num2)
    elif opcao == "2":
        print("Resultado:", num1 - num2)
    elif opcao == "3":
        print("Resultado:", num1 * num2)
    elif opcao == "4":
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("Não é possível dividir por zero!")
    else:
        print("Opção inválida.")

    # Pergunta se o usuário quer continuar
    repetir = input("Deseja fazer outra operação? (s/n): ")
    if repetir.lower() != "s":
        break