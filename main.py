def calculadora(num1,num2, operacao):
    resultado = 0
    if operacao == 1:
        resultado = num1 + num2
    elif operacao == 2:
        resultado = num1 - num2
    elif operacao == 3:
        resultado = num1 * num2
    elif operacao == 4:
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro divisao por 0")
            return 0
    else:
        print("Operacao nao especificada")
        return 0
    return resultado

while True:
    num1 = float(input("digite um numero: "))
    num2 = float(input("digite um numero: "))
    operacao = int(input("Escolha a operação (1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão): "))

    resultado = calculadora(num1, num2, operacao)

    if resultado != 0:
        print("Resultado:", resultado)

    loop = input("Deseja realizar mais alguma operacao? (s/n): ").lower()
    if loop != "s":
        print("Obg volte sempre")
        break