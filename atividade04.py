# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o 
# terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão

# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
oper = str(input('Digite o operador (+, -, *, /): '))

def calculadora(numero1, numero2, operador):
    if operador == '+':
        resultado_soma = numero1 + numero2
        return resultado_soma
    elif operador == '-':
        resultado_subtracao = numero1 - numero2
        return resultado_subtracao
    elif operador == '*':
        resultado_multiplicacao = numero1 * numero2
        return resultado_multiplicacao
    elif operador == '/':
        if numero2 != 0:
            resultado_divisao = numero1 / numero2
            return resultado_divisao
        else:
            return 'Você não pode dividir um número por 0'
    else:
        return 0  # Retorna 0 se o operador for inválido

resultado = calculadora(num1, num2, oper)

# Exibindo o resultado
if isinstance(resultado, str):  # Verifica se o resultado é uma mensagem de erro
    print(resultado)
else:
    print(f'O resultado de {num1:.2f} {oper} {num2:.2f} é: {resultado:.2f}.')