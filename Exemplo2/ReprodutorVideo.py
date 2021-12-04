import cv2 as cv
capturaVideo = cv.VideoCapture("../VideoDogao.mp4")
while True:
    verificaFrame, frameVideo = capturaVideo.read()
    cv.imshow("video",frameVideo)
    if cv.waitKey(20) & 0xFF == ord("d"): # se a tecla apertada for a tecla 20 e for "d" para o loop
        break
capturaVideo.release()
cv.destroyAllWindows()
# acontece o erro no fim da execução por conta que o opencv não encontrou mais imagens para serem apresentadas.
