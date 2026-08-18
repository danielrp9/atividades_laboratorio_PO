# 6. Faça um programa que leia e preencha 2 matrizes 10x10 (A e B) e calcule:
# somatório de A_ij * B_ij para i=1..n e j=1..n

n = 10

print("Preenchimento da Matriz A (10x10):")
matriz_a = []
for i in range(n):
    linha = []
    for j in range(n):
        valor = float(input(f"Digite o valor de A[{i+1}][{j+1}]: "))
        linha.append(valor)
    matriz_a.append(linha)

print("\nPreenchimento da Matriz B (10x10):")
matriz_b = []
for i in range(n):
    linha = []
    for j in range(n):
        valor = float(input(f"Digite o valor de B[{i+1}][{j+1}]: "))
        linha.append(valor)
    matriz_b.append(linha)

somatorio = 0
for i in range(n):
    for j in range(n):
        somatorio += matriz_a[i][j] * matriz_b[i][j]

print(f"\nResultado do somatório: {somatorio}")
