import cv2
import winsound(Works only on windows)
cam = cv2.VideoCapture(0) # Param: Index of cam that cv2 has to read
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
     # Initialise retreive and frame1, frame 2 to cam.read
    diff = cv2.absdiff(frame1, frame2)
    # Absolute difference between 2 instances(frame1, frame2) of camera to detect motion
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY) # Convert image to gray color
    blur = cv2.GaussianBlur(gray, (5,5),0) # Convert Image to blur
    # Gaussian blur params: src image, kernal size, sigma x
    var, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY) # Used to remove noise from pictures
     # Params:source image, threshold value(above which pixels are discarded), max threshold value, threshold type 
    dilated = cv2.dilate(thresh, None, iterations=3) # Threshold removes noises, but it also shrinks our object. So we dilate it. Since noise is gone, they won’t come back, but our object area increases.
    # Params: source img, kernel, no. of iterations
    contours, var = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # countour is an outline representing or bounding the shape or form of something.
    #cv2.drawContours(frame1, contours, -1, (0,255,0), 2)
    # Params:src img, contour, index(-1 to draw everything), color(RGB), thickness
    for c in contours:
        if cv2.contourArea(c) < 5000: # Ignoring smaller movements
            continue
        x, y, w, h = cv2.boundingRect(c) # For each contour we get xaxis, yaxis, width and height
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
        # Params: src image, 1st corner, 2nd corner(len = x+w, width = y+h), Color:green, thickness
        winsound.Beep(500,200 ) # Play beep sound if movement is detected
        # Frequency of beep, how longer will be the beep : 200ms 

    if cv2.waitKey(10) == ord('q'): # If user presses q then break out of the loop
        # waitkey willl display the window indefinetely until somekey is presses
        # ord is used to convert the letter to ASCII value 
        break
    cv2.imshow('Security Cam', frame1) # Param: title of popup