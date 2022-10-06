
import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image
reader = easyocr.Reader(['en'])
output = reader.readtext('rospl6.png')
for i in range(len(output)):
    print(output[i][1], end=" ")