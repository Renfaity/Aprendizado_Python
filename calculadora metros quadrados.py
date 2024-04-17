
#VARIAVEIS
# L = Largura
# A = Área
# C = Comprimento
# OP = opção
# SOP = subopção


print ("calculadora de área")
print("1 - Metros quadrados (m2)")
print("2 - Metros cubicos (m3)")
OP = int(input("Selecione a opção: "))


if OP == 1: 
    print ("1 - Calcular área (m2)")
    print ("2 - Encontrar largura")
    print ("3 - Encontrar comprimento")
    SOP = int(input("Selecione a opção: "))

    if SOP == 1:
            print ("Calculo de área (m2)")
            L = float(input("Insira a largura: "))
            C = float(input("Insira o comprimento: "))
            A = L * C
            print(A,str("m2"))

    elif SOP == 2:
            print ("Encontre a largura da área")
            A = float(input("Insira o valor da área(m2): "))
            C = float(input("Insira o comprimento da área: "))
            L= A/C
            print ("A largura é: ",L)

    elif SOP == 3:
            print ("Encontre do comprimento da área")
            A = float(input("Insira o valor da área(m2): "))
            L = float(input("Insira da largura da área: "))
            C = L/A
            print ("O comprimento é: ",C)

    else:
            print("Opção inválida")

elif OP == 2:
       print("Em contrução...")