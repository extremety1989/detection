import cv2
import pytesseract
# pytesseract.pytesseract.tesseract_cmd ='tesseract-ocr-w64-setup-5.3.1.20230401.exe'

webcam = cv2.VideoCapture(0)

if webcam.isOpened() == False:
	print('error opening the webcam')

try:
    while webcam.isOpened():
        ret, frame = webcam.read()
        if ret == True:
            imgH ,imgW,_ = frame.shape
            x1,y1,w1,h1 = 0,0,imgH ,imgW
            imgchar = pytesseract.image_to_string(frame)
            imgboxes =  pytesseract.image_to_boxes(frame)
            for boxes in imgboxes.splitlines():
                boxes = boxes.split(' ')
                x,y,w,h = int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])
                cv2.rectangle(frame,(x,imgH-y),(w,imgH-h),(0,0,255),3)
                cv2.putText(frame,imgchar,(x1 +int(w1/50),y1+int(h1/50)),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255),2) 
            cv2.imshow('text',frame)
            cv2.waitKey(1)
        else:
            break
except KeyboardInterrupt:
    pass

webcam.release()

# from PIL import Image
# plate = "L21lZGlhLXBhL1dWMTcvMS80L1dWMTcxNDM1NTgyXzEuanBlZw_rct"
# img = cv2.imread(f'./{plate}.webp',cv2.COLOR_BGR2GRAY)
# imgH ,imgW,_ = img.shape
# x1,y1,w1,h1 = 0,0,imgH ,imgW
# imgchar = pytesseract.image_to_string(img)
# imgboxes =  pytesseract.image_to_boxes(img)
# for boxes in imgboxes.splitlines():
#     boxes = boxes.split(' ')
#     x,y,w,h = int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])
#     cv2.rectangle(img,(x,imgH-y),(w,imgH-h),(0,0,255),3)
#     cv2.putText(img,imgchar,(x1 +int(w1/50),y1+int(h1/50)),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255),2) 
# print(pytesseract.image_to_string(img))
# cv2.imshow('Result',img)
# cv2.waitKey(0)