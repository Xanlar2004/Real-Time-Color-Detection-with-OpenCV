import cv2
import numpy as np

# Set the dimensions of the video frame
frame_width = 640
frame_height = 480

# Capture video from the specified camera (1)
video_capture = cv2.VideoCapture(1)
video_capture.set(3, frame_width)
video_capture.set(4, frame_height)

# Function that does nothing; used as a placeholder for trackbar callback
def placeholder_function(x):
    pass

# Create a window for HSV trackbars
cv2.namedWindow("HSV Control")
cv2.resizeWindow("HSV Control", frame_width, frame_height // 2)

# Create trackbars for adjusting HSV values
cv2.createTrackbar("HUE Low", "HSV Control", 0, 179, placeholder_function)
cv2.createTrackbar("HUE High", "HSV Control", 179, 179, placeholder_function)
cv2.createTrackbar("SAT Low", "HSV Control", 0, 255, placeholder_function)
cv2.createTrackbar("SAT High", "HSV Control", 255, 255, placeholder_function)
cv2.createTrackbar("VAL Low", "HSV Control", 0, 255, placeholder_function)
cv2.createTrackbar("VAL High", "HSV Control", 255, 255, placeholder_function)

# Main loop for video processing
while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Convert the captured frame from BGR to HSV
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Retrieve the current values from the trackbars
    h_low = cv2.getTrackbarPos("HUE Low", "HSV Control")
    h_high = cv2.getTrackbarPos("HUE High", "HSV Control")
    s_low = cv2.getTrackbarPos("SAT Low", "HSV Control")
    s_high = cv2.getTrackbarPos("SAT High", "HSV Control")
    v_low = cv2.getTrackbarPos("VAL Low", "HSV Control")
    v_high = cv2.getTrackbarPos("VAL High", "HSV Control")

    # Define the lower and upper bounds for the HSV mask
    lower_bound = np.array([h_low, s_low, v_low])
    upper_bound = np.array([h_high, s_high, v_high])
    
    # Create a mask and apply it to the original frame
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
    masked_result = cv2.bitwise_and(frame, frame, mask=mask)

    # Convert the mask to BGR for display
    mask_colored = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    
    # Stack the original image, mask, and result horizontally
    stacked_images = np.hstack([frame, mask_colored, masked_result])

    # Display the stacked images
    cv2.imshow('Stacked Output', stacked_images)
    
    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
