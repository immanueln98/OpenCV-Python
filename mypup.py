#OPRNING IMAGES WITH OPENCV IN OWN WINDOW
import cv2

img = cv2.imread("DATA/00-puppy.jpg")

while True:
    cv2.imshow('puppy',img)

    #if we waited at least 1ms and if Esc is pressed (27)
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()