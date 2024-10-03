# Otimização da Alocação de Recursos em Produção: Maximização do
# Lucro na Fabricação de Produtos A e B

import numpy as np

lucro_a = 50
lucro_b = 40

# quantidade consumida
r_A1 = 3  
r_A2 = 2  
r_B1 = 2  
r_B2 = 4  

# disponibilidade 
R1_max = 100  
R2_max = 120  

# n° simulações
num_simulations = 10000

# gerando quantidades aleatorias de A e B não exedendo seu limite
A_aleatorio = np.random.randint(0, R1_max // r_A1, num_simulations)
B_aleatorio = np.random.randint(0, R2_max // r_B2, num_simulations)

def calcular_lucro(A, B):
    return lucro_a * A + lucro_b * B

# função para verificar se respeita o limite de recursos
def verificar_restricoes(A, B):
    consumo_R1 = A * r_A1 + B * r_B1  
    consumo_R2 = A * r_A2 + B * r_B2  
    return consumo_R1 <= R1_max and consumo_R2 <= R2_max

melhor_lucro = -np.inf
melhor_A = 0
melhor_B = 0

# busca pelo melhor lucro 
for i in range(num_simulations):
    A = A_aleatorio[i]
    B = B_aleatorio[i]
    
    if verificar_restricoes(A, B):
        lucro = calcular_lucro(A, B)
        
        if lucro > melhor_lucro:
            melhor_lucro = lucro
            melhor_A = A
            melhor_B = B

print(f"A melhor combinação é produzir {melhor_A} unidades do produto A e {melhor_B} unidades do produto B.")
print(f"O lucro máximo obtido é de {melhor_lucro} unidades monetárias.")
