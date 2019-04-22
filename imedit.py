import cv2
import numpy
img = cv2.imread("/home/madelgj/Pictures/pepa.jpg", 1)
print (img.shape)
#950 55 1100 380
#we select a piece of the image
# ball = img[100:250, 55:380, :]
# # we copy that piece in ahother part of the image
# # import ipdb; ipdb.set_trace()
# img[27:177, 100:425,:] = ball
# img[:,:,2] = 0
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

edges = cv2.Canny(img,100,200)
cv2.imshow('edges', edges)
cv2.waitKey(0)

	