# 7. O valor aproximado de uma série com n termos é calculado pelo somatório:
# S = 1/4 - 3/8 + 5/16 - 7/32 + ... + (2*i - 1) / (-2)^(i+1)

n = int(input("Digite o número de termos (n > 0): "))

if n > 0:
    soma = 0.0
    for i in range(1, n + 1):
        termo = (2 * i - 1) / ((-2) ** (i + 1))
        soma += termo
    
    print(f"Valor aproximado do somatório com {n} termos: {soma}")
else:
    print("O valor de n deve ser maior que zero!")
