# -*- coding: utf-8 -*-
import cv2

def main() :
    for (i) in range(5) :
        num = str(i);
        img = cv2.imread('img/img'+num+'.jpg')

        pc_cascade = cv2.CascadeClassifier('mz80k-front/cascade.xml')

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        pces = pc_cascade.detectMultiScale(gray)

        print(pces)

        for (x,y,w,h) in pces :
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imwrite('img/output'+num+'.jpg',img)


if __name__ == '__main__' :
    main()