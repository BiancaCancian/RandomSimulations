# simular lançamento de um dado de seis lados múltiplas vezes 
# e visualizar a distribuição dos resultados

import numpy as np
import requests
import pandas as pd
import matplotlib.pyplot as plt
import random

n_lancamentos = 1000

# Gerando valores aleatorios com radom
lancamentos = np.random.randint(1, 7, n_lancamentos)

df_lancamentos = pd.DataFrame(lancamentos, columns=['Resultado'])

frequencia = df_lancamentos['Resultado'].value_counts().sort_index()

# Gerar grafico de distribuição dos resultados dos lançamentos do dado
plt.figure(figsize=(10, 6))
plt.bar(frequencia.index, frequencia.values, color='skyblue', alpha=0.7)
plt.xlabel('Resultado do Dado')
plt.ylabel('Frequência')
plt.title('Distribuição de Resultados de Lançamentos de um Dado (1000 Lançamentos)')
plt.xticks(range(1, 7))  
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()