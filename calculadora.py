print("\n\n***** Python Calculator *****")
print("\nSelecione o número da operação desejada: ")
print("\n 1 - Soma")
print("\n 2 - Subtração")
print("\n 3 - Multiplicação")
print("\n 4 - Divisão")

opcao = int(input("\nDigite sua opção (1/2/3/4): "))
num1 = 0
num2 = 0
result = 0

if(opcao == 1):
    num1 = int(input("\nDigite o primeiro numero: "))
    num2 = int(input("\nDigite o segundo numero: "))
    result = num1 + num2
    print("\nA Soma dos valores ", num1, "+", num2 , "= : ", result)
elif(opcao == 2):
    num1 = int(input("\nDigite o primeiro numero: "))
    num2 = int(input("\nDigite o segundo numero: "))
    result = num1 - num2
    print("\nA Subtração dos valores ", num1, "-", num2 , "= : ", result)
elif(opcao == 3):
    num1 = int(input("\nDigite o primeiro numero: "))
    num2 = int(input("\nDigite o segundo numero: "))
    result = num1 * num2
    print("\nA Multiplicação dos valores ", num1, "*", num2 , "= : ", result)
elif(opcao == 4):
    num1 = int(input("\nDigite o primeiro numero: "))
    num2 = int(input("\nDigite o segundo numero: "))
    result = num1 / num2
    print("\nA Divisão dos valores ", num1, "/", num2 , "= : ", result)
else:
    print("Operação não listada...")