def adicao(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multi(a,b):
    return a * b

def divisao(a,b):
    return a / b

def calculadora():
    opc = input("Escolha entre uma das operções (+,-,/,*): ")
    num1 = float(input("Informe o primeiro número: "))
    num2 = float(input("Informe o segundo número: "))

    if opc == "+":
        resultado = adicao(num1, num2)
        print(f"O resultado da adição é: {resultado}")

    elif opc == "-":
        resultado = subtracao(num1,num2)
        print(f'O resultado da subtração é: {subtracao}')

    elif opc == "*":
        resultado = multi(num1,num2)
        print(f"O resultado da multiplicação é: {multi}")

    elif opc == "/":
        resultado = divisao(num1,num2)
        print(f"O resultado da divisão é: {divisao}")
    
    else:
        print("Essa opção não existe/inválida")

conta = calculadora()

print(conta)