# 5. Escreva um programa que, para n > 0, calcule e escreva o somatório de i * (i + 1) para i de 1 a n.

n = int(input("Digite o valor de n (n > 0): "))

if n > 0:
    soma = 0
    for i in range(1, n + 1):
        soma += i * (i + 1)
    
    print(f"Resultado do somatório para n = {n}: {soma}")
else:
    print("O valor de n deve ser maior que zero!")
