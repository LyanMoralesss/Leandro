import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from colorama import Fore, Style, init

# Inicializando o colorama para cores no CMD
init(autoreset=True)

# Definindo a variável simbólica
x = sp.symbols('x')

# Etapa 1: Definindo a função L(x)
L = -x**2 + 7*x - 5
print(Fore.CYAN + Style.BRIGHT + "Passo 1: A função quadrática é definida como L(x) = -x^2 + 7x - 5.\n")

# Etapa 2: Derivando a função L(x)
L_derivada = sp.diff(L, x)
print(Fore.MAGENTA + Style.BRIGHT + f"Passo 2: Derivamos a função. A derivada de L(x) é: L'(x) = {L_derivada}.\n")

# Etapa 3: Resolvendo L'(x) = 0
solucoes = sp.solve(L_derivada, x)
print(Fore.GREEN + Style.BRIGHT + f"Passo 3: Resolvemos L'(x) = 0 para encontrar os pontos críticos. As soluções são: x = {solucoes}.\n")

# Etapa 4: Exibindo o gráfico da função
x_vals = np.linspace(-2, 10, 400)
L_vals = np.array([float(L.subs(x, val)) for val in x_vals])

plt.figure(figsize=(8, 6))
plt.plot(x_vals, L_vals, label="L(x) = -x^2 + 7x - 5", color='blue', linewidth=2)
plt.scatter([float(sol) for sol in solucoes], [float(L.subs(x, s)) for s in solucoes], color='red', s=50, label="Pontos críticos")
plt.title("Gráfico da Função L(x)", fontsize=14, color='darkblue')
plt.xlabel("x", fontsize=12)
plt.ylabel("L(x)", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

print(Fore.YELLOW + Style.BRIGHT + "Passo 4: O gráfico da função foi exibido com os pontos críticos destacados em vermelho.")
print(Style.BRIGHT + "Todas as etapas foram concluídas com sucesso.")