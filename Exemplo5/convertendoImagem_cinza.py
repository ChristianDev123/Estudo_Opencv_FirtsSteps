import cv2 as cv

imagemGatito = cv.imread("../imagemGato.jpg")
cv.imshow("Gatito Colorido", imagemGatito)

# Passando a imagem para Preto e Branco:
imagemCinza = cv.cvtColor(imagemGatito, cv.COLOR_BGR2GRAY)
cv.imshow("Gatito Cinza", imagemCinza )

# desfocando a imagem:
imagemDesfocada = cv.GaussianBlur(imagemGatito,(3,3), cv.BORDER_DEFAULT)
cv.imshow("Gatito Borrado", imagemDesfocada)

# Identificando bordas na imagem:
imagemBordas = cv.Canny(imagemGatito,125,175)
cv.imshow("Bordas do Gatito", imagemBordas)

# Diminuindo a quantidade de bordas identificadas:
imagemBordasReduzidas = cv.Canny(imagemDesfocada,125,175)
cv.imshow("Bordas da imagem desfocada", imagemBordasReduzidas)

# Dilatando linhas das bordas:
bordaDilatada = cv.dilate(imagemBordasReduzidas,(3,3),iterations=2)
cv.imshow("Bordas Dilatadas", bordaDilatada)

# Retirando Dilatação das bordas:
bordasDilatacaoReduzida = cv.erode(bordaDilatada,(3,3),iterations=2)
cv.imshow("Bordas Reduzidas", bordasDilatacaoReduzida)

# cortando uma imagem:
recorte = imagemGatito[50:300,0:500]
cv.imshow("Recorte Imagem Gatito", recorte)
cv.waitKey(0)