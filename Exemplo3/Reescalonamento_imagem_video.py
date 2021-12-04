import cv2 as cv
imagemGatito = cv.imread("../imagemGato.jpg")
videoCatchurro = cv.VideoCapture("../VideoDogao.mp4")

def redimensionamentoImagemVideo(varArquivo,escala_Porcentagem=0.75):
    largura = int(varArquivo.shape[1] * escala_Porcentagem)
    altura = int(varArquivo.shape[0] * escala_Porcentagem)
    dimensao = (largura,altura)
    return cv.resize(varArquivo,dimensao,interpolation=cv.INTER_AREA)

imagemReescalada = redimensionamentoImagemVideo(imagemGatito,0.5)
cv.imshow("Gatinho",imagemReescalada)
while True:
    verificaFrame, frame = videoCatchurro.read()
    frameReescalado = redimensionamentoImagemVideo(frame,0.5)
    cv.imshow("Dogao",frameReescalado)

    if(cv.waitKey(20) and 0xFF==ord("d")):
        break
videoCatchurro.release()
cv.destroyAllWindows()
