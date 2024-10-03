import numpy as np

def f(x1, x2):
    return x1**2 + x2**2

num_amostras = 10000

# intervalo [-10, 10] valores aleatorios

x1_amostras = np.random.uniform(-10, 10, num_amostras)
x2_amostras = np.random.uniform(-10, 10, num_amostras)

# calculo valor função
f_valor = f(x1_amostras, x2_amostras)

min_index = np.argmin(f_valor)

# ponto minimiza função
x1_min = x1_amostras[min_index]
x2_min = x2_amostras[min_index]

print(f"O valor mínimo aproximado de f(x1, x2) ocorre em (x1={x1_min}, x2={x2_min})")
print(f"O valor mínimo aproximado de f(x1, x2) é {f(x1_min, x2_min)})")