import numpy as np
# 1. CARREGAR MATRIZ DA CÂMERA
data = np.load("calibracao_camera2.npz")  # ou camera2
K = data["K"]

# 2. MATRIZES DA QUESTÃO
R = np.array([
    [0, 1, 0],
    [1, 0, 0],
    [0, 0, -1]
])

t = np.array([[0], [0], [2000]])  # mm

# montar [R | t]
RT = np.hstack((R, t))

# matriz de projeção
P = K @ RT

print("Matriz de Projeção P:\n", P)

#3. PONTOS
pontos = {
    "P1": [0, 0, 6500],
    "P2": [200, -30, 1500],
    "P3": [300, -80, 5000],
    "P4": [80, 20, 2000],
    "P5": [90, -10, 2500]
}

# 4. PROJEÇÃO
for nome, p in pontos.items():
    Pw = np.array([p[0], p[1], p[2], 1])
    img = P @ Pw

    x = img[0] / img[2]
    y = img[1] / img[2]

    dentro = (0 <= x <= 1200) and (0 <= y <= 1600)

    print(f"\n{nome}:")
    print(f"Imagem: ({x:.2f}, {y:.2f})")
    print("Dentro da imagem?" , "SIM" if dentro else "NÃO")