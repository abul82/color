import cv2
import numpy as np
image=cv2.imread('C:\\Users\\Abrar\\Downloads\\1.jpg',10)
#cv2.imshow("original",image)
#cv2.waitKey(0)

boundaries = [
    ([17, 15, 100], [50, 56, 200]),
    ( [18,50,50], [35,255,255]),
    ([86, 31, 4], [220, 88, 50]),
    ([25, 146, 190], [62, 174, 250]),
    ([103, 86, 65], [145, 133, 128])
    ]

for (lower,upper) in boundaries:
    lower=np.array(lower,dtype="uint8")
    upper=np.array(upper,dtype="uint8")
    mask=cv2.inRange(image,lower,upper)
    output=cv2.bitwise_and(image,image,mask=mask)
    cv2.imshow("mask",mask)
    cv2.imshow("images",np.hstack([image,output]))
    cv2.waitKey(0)
