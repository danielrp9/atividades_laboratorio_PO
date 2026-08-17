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

vertice = int(input(f"Digite um vértice (0 a {num_vertices - 1}): "))

if 0 <= vertice < num_vertices:
    adjacentes = []
    for j in range(num_vertices):
        if matriz[vertice][j] > 0:
            adjacentes.append(j)
    print(f"Vértices adjacentes ao vértice {vertice}: {adjacentes}")
else:
    print("Vértice inválido!")
