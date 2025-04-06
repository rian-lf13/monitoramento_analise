def criar_arquivo(registros):
    with open( 'docs/dados_paradas.txt', 'w') as arquivo:
        for registro in registros:
            linha = ', '.join(map(str, registro))
            arquivo.write(linha + '\n')