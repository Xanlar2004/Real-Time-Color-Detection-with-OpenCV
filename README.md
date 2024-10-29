<!DOCTYPE html>
<html>

<head>
  <h1>Real-Time Color Detection with OpenCV</h1>
</head>

<body>
  <h2>Introduction</h2>
  <p>This project demonstrates real-time color detection using Python and OpenCV. The program isolates and tracks specific colors in a video feed by converting RGB to HSV color space, allowing precise color detection based on hue, saturation, and value. Applications include object tracking, augmented reality, and robotics. Here are the features:<br>
     1. Real-Time Color Detection: Tracks colors in live video feeds.<br>
     2. HSV Tuning: Adjustable HSV sliders to isolate colors dynamically.<br>
     3. Applications: Supports robotics, AR, and automated color-based tracking.<br></p>
  
  <h2>Installation and Running the Code</h2>
  <p>To set up the environment:<br>
     - Download and install Visual Studio Code (or your preferred IDE).<br>
     - Install Python if not already installed.<br>
     - Install the required packages: <code>pip install numpy opencv-python</code><br>
     - Open Visual Studio Code (or your preferred IDE) and create a new file named <code>color-detection.py</code>.<br>
     - Run the application.<br></p>

  <h2>Code Explanation</h2>
  <p>This Python code enables real-time color detection through the webcam. Below is a step-by-step breakdown:<br>
     1. Imports: Import necessary libraries such as OpenCV for computer vision tasks and NumPy for handling color ranges.<br>
     2. Frame Setup: Set the frame width and height to 640x480 pixels for video clarity.<br>
     3. Trackbar Setup: Use OpenCV's trackbars to adjust HSV values dynamically, allowing flexible color range selection.<br>
     4. Main Loop: Continuously capture frames from the webcam, convert them to HSV format, and apply the selected HSV mask.<br>
     5. Display: Show the original, mask, and final images side by side to visualize the detected colors.<br>
     6. Exit: Press 'q' to exit the program and release all resources.<br></p>
  
</body>

</html>
