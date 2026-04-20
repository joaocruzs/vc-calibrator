# Calibração de Câmera com OpenCV (Método de Zhang)

Este projeto implementa a calibração de câmera utilizando o método proposto por Zhengyou Zhang, amplamente utilizado em visão computacional para estimar parâmetros intrínsecos e extrínsecos de câmeras.

---

## Objetivo

Calibrar duas câmeras (ex: celulares) a partir de imagens de um padrão plano (tabuleiro de xadrez), obtendo:

* Matriz intrínseca (K)
* Coeficientes de distorção
* Parâmetros extrínsecos (R e t)
* Correção de distorção nas imagens

---

## Estrutura do Projeto

```
projeto/
 ├── calibracao.py
 ├── camera1/
 │    ├── img1.jpg
 │    ├── img2.jpg
 │    └── ...
 ├── camera2/
 │    ├── img11.jpg
 │    ├── img12.jpg
 │    └── ...
 └── corrigidas/
```

---

## Pré-requisitos
### 1. Instalar dependências

Abra o terminal (PowerShell ou CMD) e execute:

```
python -m pip install opencv-python numpy
```

ou:

```
py -m pip install opencv-python numpy
```

---

### 2. Verificar instalação

Execute:

```
python
```

Depois:

```
import cv2
import numpy
```

Se não ocorrer erro, está tudo pronto.

---

## Coleta das Imagens

Para cada câmera:

* Tire 10 fotos (na vdd quanto mais melhor)
* Use uma imagem de tabuleiro para calibração
* Varie:

  * Ângulo
  * Distância
  * Orientação

### Observaçoes

* Não misture imagens de câmeras diferentes
* Todas as imagens devem ter a mesma resolução
* Evite imagens borradas ou com iluminação ruim

---

## Execução

Determine qual pasta de fotos deve ser usada, como por exemplo: `python calibracao.py camera1`

## O programa irá gerar:

* Matriz intrínseca (K)
* Coeficientes de distorção
* Erro RMS da calibração
* Arquivo: `calibracao_resultados.npz`
* Imagens corrigidas na pasta `corrigidas/`

---

## O método de Zhang consiste em:

1. Detectar pontos de um padrão plano (checkerboard)
2. Estimar homografias entre o plano e a imagem
3. Resolver um sistema para obter os parâmetros intrínsecos
4. Calcular parâmetros extrínsecos
5. Estimar distorção radial
6. Refinar todos os parâmetros via otimização

---

## Por fim

* Utilizar os parâmetros obtidos para projeção 3D
* Aplicar na Questão 01 do trabalho
* Comparar parâmetros entre diferentes câmeras