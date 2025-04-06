import numpy as np
from dados.registros import registros
from funcoes.arquivos import criar_arquivo
from funcoes.tratamento import tratar_arquivo
from funcoes.estatisticas import calcular_estatisticas

# Criação e tratamento dos arquivos
criar_arquivo(registros)
tratar_arquivo(registros)

# Preparar dados para análise
duracoes = np.array([int(d[2].strip()) for d in registros[1:]])

# Geração do relatório
calcular_estatisticas(duracoes)