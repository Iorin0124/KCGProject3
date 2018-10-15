# -*- coding: utf-8 -*-
import cv2

def main():

    pc_cascade = cv2.CascadeClassifier('ibm-370-138-g/cascade.xml')

    for(num) in range(62):

        img = cv2.imread('nomPic/inputPic/pic'+str(num)+'.jpg')

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        pces = pc_cascade.detectMultiScale(gray)

        print(pces)

        for (x,y,w,h) in pces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imwrite('nomPic/outputPic1/result'+str(num)+'.jpg',img)

if __name__ == '__main__' :
    main()