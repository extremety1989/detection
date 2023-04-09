import cv2

webcam = cv2.VideoCapture(0)

if webcam.isOpened() == False:
	print('[!] error opening the webcam')

try:
    while webcam.isOpened():
        ret, frame = webcam.read()
        if ret == True:
            cv2.waitKey(1)
        else:
            break
except KeyboardInterrupt:
    pass

webcam.release()