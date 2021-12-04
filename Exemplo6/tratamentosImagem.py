import cv2 as cv
import numpy as np

imagemBase = cv.imread("../imagemCidade.jpg")
cv.imshow("Imagem Base", imagemBase)

# movendo imagem pela tela e a dimminuindo (tradução):
def movimentacao(imagemFrame, posX,posY):
    matrizTraducao = np.float32([[1,0,posX],[0,1,posY]])
    dimensoes = (imagemFrame.shape[1],imagemFrame.shape[0])
    return cv.warpAffine(imagemFrame, matrizTraducao, dimensoes)
# +x = direita
# +y = baixo
# -x = esquerda
# -y = cima
imagemInferiorDireita = movimentacao(imagemBase,100,100)
cv.imshow("Imagem movimentada", imagemInferiorDireita) 

#Rotação da imagem:
def rotacaoImagem(imagemFrame,grauRotacao,pontoRotacao=None):
    altura = imagemFrame.shape[0]
    largura = imagemFrame.shape[1]
    if(pontoRotacao == None):
        pontoRotacao = (largura//2,altura//2)
    matrizRotacao = cv.getRotationMatrix2D(pontoRotacao,grauRotacao,1.0)
    dimensao = (largura,altura)
    return cv.warpAffine(imagemFrame,matrizRotacao,dimensao)
# +grau = rotacao esquerda
# -grau = rotacao direita
imagemRotacionada = rotacaoImagem(imagemBase,90)
cv.imshow("imagem Modo Retrato", imagemRotacionada)

#invertendo imagem;
imagemInvertida= cv.flip(imagemBase, 0)
cv.imshow("imagem invertida",imagemInvertida)
# 0 = girar eixo X - ponta cabeça
# 1 = girar eixo y - espelho
# -1 = girar eixo x e y - ponta cabeça e espelho;

cv.waitKey(0)