# Dado o grafo representado na imagem a seguir. 
# Faça um programa que leia um arquivo contendo
# informações do grafo, gere uma matriz de adjacência

arquivo = open("grafo.txt", "r")

primeira_linha = arquivo.readline()
num_vertices = int(primeira_linha)

matriz = []
for i in range(num_vertices):
    linha = [0] * num_vertices
    matriz.append(linha)

for linha in arquivo:
    partes = linha.split()
    origem = int(partes[0])
    destino = int(partes[1])
    peso = int(partes[2])
    
    # (ida e volta)
    matriz[origem][destino] = peso
    matriz[destino][origem] = peso

arquivo.close()

print("Matriz de Adjacência:")
for linha in matriz:
    print(linha)