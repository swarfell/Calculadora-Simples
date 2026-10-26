# Apresentação
print("--- Calculadora Simples com Python ---")
print("\033[92mgithub.com/swarfell\033[0m")

print("--------------------------------------")

# Loop do usuário
outra = "S"

while outra == "S":

    # Entrada de Dados

    num1 = float(input("| Digite o primeiro número.: "))
    num2 = float(input("| Digite o segundo número.: "))

    resultado = 0

    operacao = input("| Operação desejada (+, -, /, *, ^).: ")

    # Processamento das Operações

    match (operacao):
    # Soma
        case "+":
            resultado = num1 + num2

    # Subtração
        case "-":
            resultado = num1 - num2

    # Multiplicação
        case "*":
            resultado = num1 * num2

    # Divisão
        case "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("Divisão por zero é indefinida. ERRO!")
                resultado = None

    # Exponenciação
        case "^":
            resultado = num1 ** num2

    # Default
        case _:
            print("Sintaxe incorreta. Por favor, tente novamente!")
            resultado = None

    # Saída Geral
    if resultado is not None:
        print(f"O resultado da operação: "
              f" {num1:g} {operacao} {num2:g} é: {resultado:g}.")

        outra = input("Deseja realizar mais uma operação? S/N.: ").strip().upper()
    else:
        print("Erro de cálculo. Por favor, tente novamente.")

print("Obrigado por ter usado ;)")
print("Até mais!")
