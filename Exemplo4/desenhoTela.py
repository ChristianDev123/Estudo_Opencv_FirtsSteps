import cv2 as cv
import numpy as np

ambiente = np.zeros((720,1080,3), dtype="uint8")
# Pintando a Tela inteira:
ambiente[:] = (0,0,0)
# Desenhando um Retângulo:
cv.rectangle(ambiente,(0,0),(ambiente.shape[1]//2,ambiente.shape[0]//2),(0,0,255),-1)
# Desenhando um círculo:
cv.circle(ambiente,(ambiente.shape[1]//4,ambiente.shape[0]//4),150,(255,255,255),thickness=7)
# Desenhndo uma Linha:
cv.line(ambiente,(0,0),(ambiente.shape[1]//2,ambiente.shape[0]//2),(255,255,255),thickness=7)
# Escrevendo na Tela:
cv.putText(ambiente, "Uma vez Flamengo, sempre Flamengo, Flamengo sempre hei de ser...", (0,ambiente.shape[0]//2 +50), cv.FONT_HERSHEY_TRIPLEX, 0.75, (0,0,255), 2)

cv.imshow("Blank",ambiente)
cv.waitKey(0)