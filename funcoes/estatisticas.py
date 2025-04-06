import numpy as np

def calcular_estatisticas(duracoes):
    media = np.mean(duracoes)
    mediana = np.median(duracoes)
    desvio = np.std(duracoes)

    recomendacoes = []

    if media >= 8:
        recomendacoes.append("- A média esta alta. Reforce manutencoes preventivas.")
    if desvio >= 3:
        recomendacoes.append("- Alta variacao nas paradas. Investigar causas especificas.")
    if np.count_nonzero(duracoes[:5] > 6) >= 3 or np.count_nonzero(duracoes[-5:] > 6) >= 3:
        recomendacoes.append("- Muitas paradas no inicio/fim do dia. Avaliar rotinas nesses horarios.")

    with open('docs/relatorio.txt', 'w') as relatorio:
        relatorio.write("Relatorio de Estatisticas das Paradas\n")
        relatorio.write("-------------------------------------\n")
        relatorio.write(f"Media: {media:.2f} minutos\n")
        relatorio.write(f"Mediana: {mediana:.2f} minutos\n")
        relatorio.write(f"Desvio Padrao: {desvio:.2f} minutos\n\n")
        relatorio.write("Recomendacoes:\n")
        if recomendacoes:
            for r in recomendacoes:
                relatorio.write(r + '\n')
        else:
            relatorio.write("Nenhuma acao necessaria.\n")

    return media, mediana, desvio