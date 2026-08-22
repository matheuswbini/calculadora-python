"""
Calculadora simples em Python, com menu no terminal.

Como executar:
    python calculadora.py
"""


def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        print("Erro: não é possível dividir por zero.")
        return None
    return a / b


def ler_numero(mensagem):
    """Pede um número ao usuário, repetindo até receber um valor válido."""
    while True:
        entrada = input(mensagem)
        try:
            return float(entrada)
        except ValueError:
            print("Valor inválido. Digite um número (ex: 3 ou 3.5).")


def mostrar_menu():
    print("\n===== CALCULADORA =====")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")
    print("========================")


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Até logo!")
            break

        if opcao not in ("1", "2", "3", "4"):
            print("Opção inválida. Tente novamente.")
            continue

        a = ler_numero("Digite o primeiro número: ")
        b = ler_numero("Digite o segundo número: ")

        if opcao == "1":
            print(f"Resultado: {soma(a, b)}")
        elif opcao == "2":
            print(f"Resultado: {subtracao(a, b)}")
        elif opcao == "3":
            print(f"Resultado: {multiplicacao(a, b)}")
        elif opcao == "4":
            resultado = divisao(a, b)
            if resultado is not None:
                print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
