import cv2
import numpy as np

def sketch(image):

    ### first convert it to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ## Cleaning up the image by gaussian blur
    blurr = cv2.GaussianBlur(gray, (5,5), 0)

    ## Extracting the edges
    cannyy =  cv2.Canny(blurr, 10, 70)

    ##Do the invert binarize the IMAGE
    ret, mask = cv2.threshold(cannyy, 70, 255, cv2.THRESH_BINARY_INV)

    return(mask)


cap = cv2.VideoCapture(0)
while True :

  ret, frame = cap.read()
  cv2.imshow("INPUT_IMAGE", frame)
  cv2.imshow("FINAL_SKETCHED_IMAGE", sketch(frame))
  if cv2.waitKey(1) == 13:  ## key 13 is for enter
     break

cap.release()
cv2.destroyAllWindows()
