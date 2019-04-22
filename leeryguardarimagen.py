import cv2
#we read an image from the PC, the 0 stands for gray
img = cv2.imread("/home/madelgj/Pictures/asrob.png",0)
#as we know our image doesn't fit well with autosized window, we normalize it, in other case, this step would not be necessary
#namedWindow(name of the window, 'size')
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
#We wait until a key is pressed for uploading the image
#cv2.waitKey(2000)
#we will try to use waitkey for several things
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('asrobgray2.png',img)
    cv2.destroyAllWindows()