import cv2
import numpy as np

# Set the dimensions of the video frame
frame_width = 640
frame_height = 480

# Function to initialize video capture
def initialize_video_capture(camera_index=0):
    cap = cv2.VideoCapture(camera_index)
    cap.set(3, frame_width)
    cap.set(4, frame_height)
    return cap

# Function that does nothing; used as a placeholder for trackbar callback
def placeholder_function(x):
    pass

# Function to create trackbars for HSV control
def create_hsv_trackbars():
    cv2.namedWindow("HSV Control")
    cv2.resizeWindow("HSV Control", frame_width, frame_height // 2)

    cv2.createTrackbar("HUE Low", "HSV Control", 0, 179, placeholder_function)
    cv2.createTrackbar("HUE High", "HSV Control", 179, 179, placeholder_function)
    cv2.createTrackbar("SAT Low", "HSV Control", 0, 255, placeholder_function)
    cv2.createTrackbar("SAT High", "HSV Control", 255, 255, placeholder_function)
    cv2.createTrackbar("VAL Low", "HSV Control", 0, 255, placeholder_function)
    cv2.createTrackbar("VAL High", "HSV Control", 255, 255, placeholder_function)

# Function to get current HSV values from trackbars
def get_hsv_values():
    h_low = cv2.getTrackbarPos("HUE Low", "HSV Control")
    h_high = cv2.getTrackbarPos("HUE High", "HSV Control")
    s_low = cv2.getTrackbarPos("SAT Low", "HSV Control")
    s_high = cv2.getTrackbarPos("SAT High", "HSV Control")
    v_low = cv2.getTrackbarPos("VAL Low", "HSV Control")
    v_high = cv2.getTrackbarPos("VAL High", "HSV Control")
    return (h_low, h_high, s_low, s_high, v_low, v_high)

# Function to create a mask based on HSV values
def create_mask(hsv_image, hsv_values):
    h_low, h_high, s_low, s_high, v_low, v_high = hsv_values
    lower_bound = np.array([h_low, s_low, v_low])
    upper_bound = np.array([h_high, s_high, v_high])
    return cv2.inRange(hsv_image, lower_bound, upper_bound)

# Function to display stacked images
def display_stacked_images(original, mask, result):
    mask_colored = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    stacked_images = np.hstack([original, mask_colored, result])
    cv2.imshow('Stacked Output', stacked_images)

# Main function
def main():
    video_capture = initialize_video_capture(1)
    create_hsv_trackbars()

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Convert the captured frame from BGR to HSV
        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Retrieve the current HSV values from the trackbars
        hsv_values = get_hsv_values()

        # Create mask based on current HSV values
        mask = create_mask(hsv_image, hsv_values)
        masked_result = cv2.bitwise_and(frame, frame, mask=mask)

        # Display the stacked images
        display_stacked_images(frame, mask, masked_result)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close all OpenCV windows
    video_capture.release()
    cv2.destroyAllWindows()

# Run the main function
if __name__ == "__main__":
    main()
