# animacion_funcion.py

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import time

# ------------------ ENTRADA ------------------
x = sp.symbols('x')

# Funciones predefinidas
funciones = {
    "1": "sin(x)",
    "2": "cos(x)",
    "3": "x**2",
    "4": "log(x+1)",
    "5": "exp(x)",
    "6": "x**3 - 3*x"
}

print("Elegí una función o escribí la tuya:")
for clave, fstr in funciones.items():
    print(f"{clave}: {fstr}")
f_input = input("Opción o función: ")

if f_input in funciones:
    f_str = funciones[f_input]
else:
    f_str = f_input

f = sp.sympify(f_str)

# Rango de x y paso
x_ini = float(input("x inicial: "))
x_fin = float(input("x final: "))
paso = float(input("Paso: "))

# Límites de y personalizados (opcional)
usar_limites_y = input("¿Querés definir límites personalizados para el eje y? (s/n): ").strip().lower()
if usar_limites_y == 's':
    y_min = float(input("Valor mínimo de y: "))
    y_max = float(input("Valor máximo de y: "))
else:
    y_min = None
    y_max = None

# ------------------ CÁLCULO ------------------
valores_x = np.arange(x_ini, x_fin + paso, paso)
valores_y = [float(f.subs(x, val)) for val in valores_x]

# ------------------ GRAFICADO ------------------
plt.ion()
fig, ax = plt.subplots()

ax.set_xlim(x_ini, x_fin)
if y_min is not None and y_max is not None:
    ax.set_ylim(y_min, y_max)
else:
    ax.set_ylim(min(valores_y) - 1, max(valores_y) + 1)

ax.axhline(0, color='gray', linewidth=0.8)  # eje x
ax.axvline(0, color='gray', linewidth=0.8)  # eje y
ax.grid(True)
ax.set_title("Gráfico de f(x)")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.legend([f"f(x) = {f_str}"])

linea, = ax.plot([], [], 'ro',markersize=3)
x_vals = []
y_vals = []

# ------------------ ANIMACIÓN ------------------
for xi, yi in zip(valores_x, valores_y):
    x_vals.append(xi)
    y_vals.append(yi)
    linea.set_data(x_vals, y_vals)
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.1)

plt.ioff()
plt.show()

