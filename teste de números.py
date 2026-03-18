import random

print ("Teste de números")
n = 0
while n < 100:
    print ("Tentativa nº:",n)
    n = n+1
    numero = random.randint(0,100)
    print (numero)
    if numero % 2 == 0:
            print ("O número é PAR")
    else:
            print ("O número é ÍMPAR")

