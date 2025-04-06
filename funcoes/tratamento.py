def tratar_arquivo(registros):
    with open('docs/dados_paradas.txt', 'w') as arquivo:
        for i, registro in enumerate(registros):
            if i == 0:
                continue
            linha = f"Data: {registro[0]}, Hora: {registro[1]}, Duracao: {registro[2]} minutos\n"
            arquivo.write(linha)