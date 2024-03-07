# Nome do arquivo que você deseja ler (altere para o caminho/nome do seu arquivo)
file_names = [
    '1.1-importância.txt',
    '1.2-Escopo.txt']


nome_arquivo = file_names[0]
nome_arquivo = file_names[1]


try:
    # Abre o arquivo em modo de leitura
    with open(nome_arquivo, 'r') as arquivo:
        # Lê o conteúdo do arquivo
        conteudo = arquivo.read()
        # Imprime o conteúdo
        print(conteudo)
except FileNotFoundError:
    print(f'O arquivo {nome_arquivo} não foi encontrado.')
except Exception as e:
    print(f'Ocorreu um erro: {e}')
