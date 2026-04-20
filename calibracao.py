import cv2
import numpy as np
import glob
import os
import sys

NX = 5
NY = 8  
SQUARE_SIZE = 30  
if len(sys.argv) < 2:
    print("Uso: python calibracao.py camera1 ou camera2")
    sys.exit()

CAMERA = sys.argv[1]
IMAGE_FOLDER = f"{CAMERA}/*.jpeg"

# 1. PONTOS 3D
objp = np.zeros((NX * NY, 3), np.float32)
objp[:, :2] = np.mgrid[0:NX, 0:NY].T.reshape(-1, 2)
objp *= SQUARE_SIZE

objpoints = []
imgpoints = []

# 2. LEITURA DAS IMAGENS
images = glob.glob(IMAGE_FOLDER)

if len(images) == 0:
    print(f"Não encontrei imagens em {IMAGE_FOLDER}")
    sys.exit()

print(f"{len(images)} imagens encontradas em {CAMERA}")

# 3. DETECÇÃO DOS CANTOS
valid_images = 0

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, (NX, NY), None)

    if ret:
        valid_images += 1
        objpoints.append(objp)

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)

        cv2.drawChessboardCorners(img, (NX, NY), corners2, ret)
        cv2.imshow(f'Detecção - {CAMERA}', img)
        cv2.waitKey(200)

    else:
        print(f"❌ Não encontrou tabuleiro em: {fname}")

cv2.destroyAllWindows()

# * CHECAGEM IMPORTANTE
if valid_images == 0:
    print("\nERRO: Nenhuma imagem válida para calibração!")
    print("Verifique o tabuleiro e NX/NY.")
    sys.exit()

print(f"\n✔ {valid_images} imagens válidas para calibração")

# 4. CALIBRAÇÃO
ret, K, dist, rvecs, tvecs = cv2.calibrateCamera(
    objpoints,
    imgpoints,
    gray.shape[::-1],
    None,
    None
)

# 5. RESULTADOS
print("\n==============================")
print(f"RESULTADOS - {CAMERA}")
print("==============================")

print("\nMatriz Intrínseca (K):")
print(K)

print("\nCoeficientes de Distorção:")
print(dist)

print("\nErro RMS:")
print(ret)

# 6. SALVAR RESULTADOS
output_file = f"calibracao_{CAMERA}.npz"

np.savez(output_file,
         K=K,
         dist=dist,
         rvecs=rvecs,
         tvecs=tvecs)

print(f"\nResultados salvos em '{output_file}'")

# 7. CORREÇÃO DE IMAGENS
output_folder = f"corrigidas_{CAMERA}"
os.makedirs(output_folder, exist_ok=True)

for fname in images:
    img = cv2.imread(fname)
    h, w = img.shape[:2]

    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(K, dist, (w, h), 1, (w, h))

    dst = cv2.undistort(img, K, dist, None, newcameramtx)

    x, y, w_roi, h_roi = roi
    dst = dst[y:y+h_roi, x:x+w_roi]

    output_name = os.path.join(output_folder, os.path.basename(fname))
    cv2.imwrite(output_name, dst)

print(f"Imagens corrigidas salvas em '{output_folder}'")
