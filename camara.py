import cv2
cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
#name,fourcc,framespersecond,frame size
out = cv2.VideoWriter('prueba.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret == True:

    	# Our operations on the frame come here in real time

        frame = cv2.flip(frame,0)
        #XQ NO DEJA GUARDAR EN BLANCO Y NEGRO?
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # write the flipped frame
        #SI PONES GRAY NO VA
        out.write(frame)

    	# Display the resulting frame in streaming and we have our video in gray
    	#HACER VARIAS OPERACIONES CON LLAMADAS DE RETORNO
       	cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


    #to get the width and height of the frames cap.get(number bt 0 to 18) denotes a property of the capture
    width = cap.get(3) #640
    height = cap.get(4) #480
    print(width)
    print(height)

    #now we want the frames to be half the width and height:
    #ret = cap.set(3,320)
    #ret = cap.set(4,240)
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

