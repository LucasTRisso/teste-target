var = int(input("DIgite um número: "))
soma = 0
x = 1

while soma <= var:
    if soma == var:
        print("Seu número pertence à sequência de Fibonacci!")
    soma = soma + x
    x = soma - x

if soma > var and var != x:
    print("Seu número não pertence à sequência de Fibonacci.")
    

