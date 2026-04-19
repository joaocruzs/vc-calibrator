import cv2
import numpy as np
import glob
import os

NX = 9
NY = 6
SQUARE_SIZE = 30
IMAGE_FOLDER = "camera1/*.jpg"

# 1. PREPARAÇÃO DOS PONTOS 3D
objp = np.zeros((NX * NY, 3), np.float32)
objp[:, :2] = np.mgrid[0:NX, 0:NY].T.reshape(-1, 2)
objp *= SQUARE_SIZE

objpoints = []
imgpoints = []

# 2. LEITURA DAS IMAGENS
images = glob.glob(IMAGE_FOLDER)

if len(images) == 0:
    print("Não encontrei as imagens :(")
    exit()

print(f"{len(images)} Encontrei as imagens :)")

# 3. DETECÇÃO DOS CANTOS
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, (NX, NY), None)

    if ret:
        objpoints.append(objp)

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)

        cv2.drawChessboardCorners(img, (NX, NY), corners2, ret)
        cv2.imshow('Detecção', img)
        cv2.waitKey(300)

    else:
        print(f"Não encontrei o Tabuleiro em: {fname}")

cv2.destroyAllWindows()

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
print("RESULTADOS DA CALIBRAÇÃO")
print("==============================")

print("\n Matriz Intrínseca (K):")
print(K)

print("\n Coeficientes de Distorção:")
print(dist)

print("\n Erro RMS:")
print(ret)

# 6. SALVAR RESULTADOS
np.savez("calibracao_resultados.npz",
         K=K,
         dist=dist,
         rvecs=rvecs,
         tvecs=tvecs)

print("\n Resultados salvos em 'calibracao_resultados.npz'")

# 7. TESTE: REMOVER DISTORÇÃO
os.makedirs("corrigidas", exist_ok=True)

for fname in images:
    img = cv2.imread(fname)
    h, w = img.shape[:2]

    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(K, dist, (w, h), 1, (w, h))

    dst = cv2.undistort(img, K, dist, None, newcameramtx)

    x, y, w, h = roi
    dst = dst[y:y+h, x:x+w]

    output_name = os.path.join("corrigidas", os.path.basename(fname))
    cv2.imwrite(output_name, dst)

print("Imagens corrigidas salvas na pasta 'corrigidas'")
