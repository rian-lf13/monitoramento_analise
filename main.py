import numpy as np

registros = np.array([
    ["Data", "Hora" , "Duração"],

    ["2025-03-01", "08:15", "5"], #"Parada breve no início do turno, pode indicar pequenos ajustes iniciais da máquina"
    ["2025-03-01", "10:45"," 8"], #"Parada ocorrida no meio do turno, sugerindo um possível desgaste gradual"
    ["2025-03-01", "14:20"," 3"], #"Parada curta no período pós-almoço, menos impactante"
    ["2025-03-02", "07:50"," 7"], #"Parada logo no início da manhã, possivelmente associada à preparação dos equipamentos"
    ["2025-03-02", "09:30", "12"], #"Parada com duração maior, indicando que algum problema não foi resolvido rapidamente"
    ["2025-03-02", "15:10"," 6"], #"Registro de parada à tarde, que pode ser sinal de desgaste ou ajuste de processo"
    ["2025-03-03", "08:05"," 4"], #"Início de turno com parada leve"
    ["2025-03-03", "11:45"," 9"], #"Parada média antes do pico de produção, importante para identificar padrões de lentidão"
    ["2025-03-03", "16:30", "10"], #"Parada ocorrida no final do turno, sugerindo que a máquina pode estar acumulando desgaste ao longo do dia"
    ["2025-03-04", "07:45"," 8"], #"Parada no início do turno com duração considerável, que pode ser analisada em conjunto com outras ocorrências matinais"
    ["2025-03-04", "12:00"," 5"], #"Parada ao meio-dia, talvez devido a uma pequena verificação de rotina"
    ["2025-03-04", "17:20", "7"], #"Parada no final do dia, reforçando a hipótese de cansaço ou desgaste dos equipamentos ao longo do dia"
    ["2025-03-05", "08:10", "6"], #"Parada breve na abertura do expediente"
    ["2025-03-05", "10:30", "10"], #"Parada média com potencial impacto na produtividade, demandando análise detalhada"
    ["2025-03-05", "15:50"," 9"], #"Parada no período da tarde, indicando um padrão semelhante ao observado em dias anteriores"
])

def criar():
    with open('docs/dados_paradas.txt', 'w') as arquivo:
        for registro in registros:
            linha = ', '.join(map(str, registro))  # Converte cada elemento em string e junta com ', '
            arquivo.write(linha + '\n')

# Tratamento dos dados 

def tratamento():
    with open('docs/dados_paradas.txt', 'w') as arquivo:
        for indice, registro in enumerate(registros):
            if indice == 0:
                continue  # Pula o cabeçalho
            linha = f"Data: {registro[0]}, Hora: {registro[1]}, Duração: {registro[2]} minutos \n"
            arquivo.write(linha)

duracoes_str = registros[1:, 2]
duracoes = np.array([int(duracao.strip()) for duracao in duracoes_str])

def estatistica():
    media = np.mean(duracoes)
    mediana = np.median(duracoes)
    desvio_padrao = np.std(duracoes)

    #cria e escreve um relatório
    with open('docs/relatorio.txt', 'w') as relatorio:
                relatorio.write("Relatorio de Estatisticas das Paradas\n")
                relatorio.write("-----------------------------------\n")
                relatorio.write(f"Media: {media:.2f} minutos\n")
                relatorio.write(f"Mediana: {mediana:.2f} minutos\n")
                relatorio.write(f"Desvio Padrao: {desvio_padrao:.2f} minutos\n")
    
    return {
        "media": media,
        "mediana": mediana,
        "desvio_padrao": desvio_padrao
    }

