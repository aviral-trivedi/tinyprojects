import cv2
import numpy as np
import time

# Define coordinates of region of interest
# x = 400 
# y = 380 
# w_crop = 500  # width of cropped region
# h_crop = 500  # height of cropped region

# Define coordinates of the ignored rectangle area
ignore_x = 350
ignore_y = 250
ignore_width = 170  # width of the rectangle
ignore_height = 500  # height of the rectangle

# Function for frame and lanes
def detect_lanes(frame):
    # Resize the frame to half of its original size
    frame = cv2.resize(frame, None, fx=0.6, fy=0.6)

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply Canny edge detection
    edges = cv2.Canny(blur, 200, 200)
    
    # Define a region of interest (ROI) polygon
    height, width = edges.shape[:2]
    vertices = np.array([[0, 380], [300, 240], [450, 240], [720, 420]])
    roi_mask = np.zeros_like(edges)
    cv2.fillPoly(roi_mask, [vertices], 255)
    
    # Create a mask for the ignored rectangle area
    cv2.rectangle(roi_mask, (ignore_x, ignore_y), (ignore_x + ignore_width, ignore_y + ignore_height), 0, -1)
    
    # Apply the ROI mask to the edges
    masked_edges = cv2.bitwise_and(edges, roi_mask)

    # Apply Hough transform to detect lines
    lines = cv2.HoughLinesP(masked_edges, rho=2, theta=np.pi/180, threshold=60, minLineLength=100, maxLineGap=50)
    
    # Draw the detected lines on the frame
    lane_lines = np.zeros_like(frame)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(lane_lines, (x1, y1), (x2, y2), (255, 255, 0), 3)
    
    # Combine the detected lanes with the original frame
    result = cv2.addWeighted(frame, 0.8, lane_lines, 1, 0)
    
    return result


# Open a video file
video_path = "/home/cleon/Local Files/Drive Safe/test4.mp4"
cap = cv2.VideoCapture(video_path)

# Process each frame in the video
while cap.isOpened():
    ret, frame = cap.read()
    time.sleep(1 / 80)
    if not ret:
        # Reset video capture to loop the video
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue
    
    # Detect lanes in the current frame
    result = detect_lanes(frame)
    
    # Display the result
    cv2.namedWindow("Lane Detection", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Lane Detection", 700, 450)
    cv2.imshow("Lane Detection", result)
    
    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
