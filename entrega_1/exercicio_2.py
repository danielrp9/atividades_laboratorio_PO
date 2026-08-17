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

print("Grau de cada vértice:")
for i in range(num_vertices):
    grau = 0
    for j in range(num_vertices):
        if matriz[i][j] > 0:
            grau = grau + 1
    print(f"Vértice {i}: grau {grau}")
