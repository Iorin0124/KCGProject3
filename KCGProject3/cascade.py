import cv2

pc_cascade = []
name = ['mz80-k', 'ibm370-138', 'dynabook386-20']
result = ""


def main():
    if len(pc_cascade) == 0:
        pc_cascade.append(cv2.CascadeClassifier('mz80k-front-c/cascade.xml'))
        pc_cascade.append(cv2.CascadeClassifier('ibm370-138-e/cascade.xml'))
        pc_cascade.append(cv2.CascadeClassifier('dynabook386-20-f/cascade.xml'))

    for (x) in range(4):
        result = ""
        flg = True

        img = cv2.imread('inputPic/img'+str(x)+'.jpg')

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        for (count) in range(len(pc_cascade)):
            result = pc_cascade[count].detectMultiScale(gray)

            if len(result) != 0:
                for (x,y,w,h) in result:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

                cv2.imwrite('outputPic/'+str(count)+'result'+str(x)+name[count]+'.jpg',img)

                print(name[count])

                flg=False

                break
        if (flg):
            print('none')


main()