import cv2
import numpy as np


#color ranges
lower_red_d = np.array([0,150,50])
upper_red_d = np.array([5,255,255])

lower_red = np.array([170,150,50])
upper_red = np.array([180,255,255])

lower_blue = np.array([94,80,2])
upper_blue = np.array([126,255,255])


cap = cv2.VideoCapture('one_round_cam.mp4')

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 50.0, (1920,1080), True)

while(cap.isOpened()):

    ret, frame = cap.read()

    if not ret:
        print("No more frames left.")
        break
        
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_red1 = cv2.inRange(hsv, lower_red, upper_red)
    mask_red2 = cv2.inRange(hsv, lower_red_d, upper_red_d)
    mask = mask1 + mask_red1 + mask_red2
    
    res = cv2.bitwise_and(frame,frame, mask= mask)
    out.write(res)
    cv2.imshow('res',res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
out.release()
print("Video saved successfully.")
cv2.destroyAllWindows() 