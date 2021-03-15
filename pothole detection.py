import numpy
import cv2
from matplotlib import pyplot as plt

image_number=1
img=1

while (type(img)!=type(None)):
    img = cv2.imread(('K:\TY_I_shraddha\sem 1\CV\pothole/pothole_')+str(image_number)+'.jpeg')#image1
    plt.subplot(3, 2, 1), plt.imshow(img, 'gray')


    blur = cv2.blur(img,(5,5))
    gblur = cv2.GaussianBlur(img,(5,5),0)
    median = cv2.medianBlur(img,5)

    kernel = numpy.ones((5,5),numpy.uint8)
    erosion = cv2.erode(median,kernel,iterations = 1)
    dilation = cv2.dilate(erosion,kernel,iterations = 5)
    closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)

    edges = cv2.Canny(closing,9,420)
    #edges = cv2.Canny(dilation,9,120)

    ret,threshold=cv2.threshold(edges.copy(),0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    contours,_=cv2.findContours(threshold,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(img,contours,-1,(0,0,255),2)
    cv2.imshow("Show",img)

    plt.subplot(3, 2, 2), plt.imshow(median, 'gray')
    plt.subplot(3, 2, 3), plt.imshow(erosion, 'gray')
    plt.subplot(3, 2, 4), plt.imshow(dilation, 'gray')
    plt.subplot(3, 2, 5), plt.imshow(closing, 'gray')
    plt.subplot(3, 2, 6), plt.imshow(edges, 'gray')

    plt.show()

    image_number += 1

cv2.waitKey()#to hold image
