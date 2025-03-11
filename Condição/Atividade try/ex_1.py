num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
operacao = input("Digite a operação desejada (+, -, * ou /): ")
def calculadora(num1, num2, operacao):
    try:
        num1 = float(num1)
        num2 = float(num2)
        
        if operacao == '+':
            return num1 + num2
        elif operacao == '-':
            return num1 - num2
        elif operacao == '*':
            return num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError("Erro: Divisão por zero não é permitida.")
            return num1 / num2
        else:
            raise ValueError("Erro: Operação inválida. Use +, -, * ou /.")
    
    except ValueError:
        return "Erro: Entrada inválida. Certifique-se de inserir números válidos."
    except ZeroDivisionError as e:
        return str(e)
print(calculadora(num1, num2, operacao))