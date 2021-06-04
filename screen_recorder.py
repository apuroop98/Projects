from PIL import ImageGrab # Pillow is a package that adds support for opening, manipulating and saving many different image file formats.
import numpy as np  # NumPy is a library used for adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
import cv2      # Open cv  is used to work with Computer vision and Img related problems.

while(True):
    img = ImageGrab.grab(bbox =(0,0,1280,720) )  # Calling Image grab to grab screen in the specified dimensions
    # Parameters:min corner, maxcorner, width height
    img_np = np.array(img)  # Convert imager to numpy array to store image related info.
    img_final  = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)  # Takes input and converts it to RGB Color
    cv2.imshow('Screen recorder', img_final)    # Call cv2 to show an Img
    # Parameters: name of screen recording software,Array you want to display
    cv2.waitKey(10) # Wait till user presses a key
    # Parameters: delay in milliseconds
