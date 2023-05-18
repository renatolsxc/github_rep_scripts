import csv

# Nome do arquivo original e do arquivo de saída
arquivo_original = 'C:\\Users\\renato\\Desktop\\output-umacoluna.csv'
arquivo_saida = 'C:\\Users\\renato\\Desktop\\output-umacoluna_saida.csv'

# Lista para armazenar os elementos do arquivo original
elementos = []

# Variável para armazenar o elemento atual
elemento_atual = []

# Ler o arquivo original e armazenar os elementos na lista
with open(arquivo_original, 'r') as f:
    num_linhas_elemento = 4

    for linha in f:
        objeto = linha.strip()
        elemento_atual.append(objeto)

        # Verificar se todas as linhas do elemento foram lidas
        if len(elemento_atual) == num_linhas_elemento:
            elementos.append(elemento_atual)
            elemento_atual = []

# Verificar se o número de elementos está correto
#if len(elementos) != 6800:
#    print("O número de elementos não está correto. Verifique o arquivo original.")
#    exit()

# Escrever os dados no arquivo de saída
with open(arquivo_saida, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(elementos)

print("Arquivo de saída criado com sucesso!")
