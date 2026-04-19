# 📷 Calibração de Câmera com OpenCV (Método de Zhang)

Este projeto implementa a calibração de câmera utilizando o método proposto por Zhengyou Zhang, amplamente utilizado em visão computacional para estimar parâmetros intrínsecos e extrínsecos de câmeras.

---

## 📌 Objetivo

Calibrar duas câmeras (ex: celulares) a partir de imagens de um padrão plano (tabuleiro de xadrez), obtendo:

* Matriz intrínseca (K)
* Coeficientes de distorção
* Parâmetros extrínsecos (R e t)
* Correção de distorção nas imagens

---

## 📂 Estrutura do Projeto

```
projeto/
 ├── calibracao.py
 ├── celular1/
 │    ├── img1.jpg
 │    ├── img2.jpg
 │    └── ...
 ├── celular2/
 │    ├── img1.jpg
 │    ├── img2.jpg
 │    └── ...
 └── corrigidas/
```

---

## ⚙️ Pré-requisitos

### 1. Instalar Python

Baixe e instale o Python:

https://www.python.org/downloads/

⚠️ Durante a instalação, marque:

```
✔ Add Python to PATH
```

---

### 2. Instalar dependências

Abra o terminal (PowerShell ou CMD) e execute:

```
python -m pip install opencv-python numpy
```

ou:

```
py -m pip install opencv-python numpy
```

---

### 3. Verificar instalação

Execute:

```
python
```

Depois:

```
import cv2
import numpy
```

Se não ocorrer erro, está tudo pronto ✅

---

## 📸 Coleta das Imagens

Para cada câmera:

* Tire entre **10 e 20 fotos**
* Use um **tabuleiro de xadrez impresso**
* Varie:

  * Ângulo
  * Distância
  * Orientação

### ⚠️ Importante

* Não misture imagens de câmeras diferentes
* Todas as imagens devem ter a **mesma resolução**
* Evite imagens borradas ou com iluminação ruim

---

## ▶️ Execução

### 1. Configure a pasta de imagens

No arquivo `calibracao.py`, altere:

```
IMAGE_FOLDER = "celular1/*.jpg"
```

Para calibrar a segunda câmera:

```
IMAGE_FOLDER = "celular2/*.jpg"
```

---

### 2. Executar o script

No terminal:

```
python calibracao.py
```

---

## 📊 Saídas do Programa

O programa irá gerar:

* Matriz intrínseca (K)
* Coeficientes de distorção
* Erro RMS da calibração
* Arquivo: `calibracao_resultados.npz`
* Imagens corrigidas na pasta `corrigidas/`

---

## 🧠 Método Utilizado

O método de Zhang consiste em:

1. Detectar pontos de um padrão plano (checkerboard)
2. Estimar homografias entre o plano e a imagem
3. Resolver um sistema para obter os parâmetros intrínsecos
4. Calcular parâmetros extrínsecos
5. Estimar distorção radial
6. Refinar todos os parâmetros via otimização

---

## 💡 Dicas

* Use pelo menos 10 imagens por câmera
* Quanto maior a variedade de ângulos, melhor o resultado
* Evite que o padrão fique sempre paralelo à câmera
* Prefira imagens com boa iluminação

---

## 🚀 Próximos Passos

* Utilizar os parâmetros obtidos para projeção 3D
* Aplicar na Questão 01 do trabalho
* Comparar parâmetros entre diferentes câmeras

---

## 👨‍💻 Autor

Projeto desenvolvido para disciplina de Visão Computacional – UFPI
