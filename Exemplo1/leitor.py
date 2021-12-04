import cv2 as cv
img = cv.imread("../imagemGato.jpg") # pega a foto e identifica o tamanho dela
cv.imshow("Gatinho", img) # executa a Imagem numa janela separada, primeiro parâmetro = nome tela, segundo parâmetro = tamanho da imagem e endereço
cv.waitKey(0) # serve para o programa esperar infinitamente por uma tecla