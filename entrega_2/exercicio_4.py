arquivo = open("grafo.txt", "r")

num_vertices = int(arquivo.readline())

matriz = []
for i in range(num_vertices):
    matriz.append([0] * num_vertices)

for linha in arquivo:
    partes = linha.split()
    origem = int(partes[0])
    destino = int(partes[1])
    peso = int(partes[2])
    
    matriz[origem][destino] = peso
    matriz[destino][origem] = peso

arquivo.close()

n = int(input("Digite a quantidade de itinerários (n): "))

for i in range(n):
    entrada = input(f"\nDigite as cidades do itinerário {i+1} separadas por espaço (ex: 0 5 1 0 4 1): ")
    cidades = [int(x) for x in entrada.split()]
    
    custo_total = 0
    valido = True
    
    for j in range(len(cidades) - 1):
        origem = cidades[j]
        destino = cidades[j+1]
        
        peso = matriz[origem][destino]
        if peso > 0:
            custo_total += peso
        else:
            print(f"Não há ligação direta entre a cidade {origem} e a cidade {destino}!")
            valido = False
            break
            
    if valido:
        print(f"Custo total do itinerário {i+1}: {custo_total}")
