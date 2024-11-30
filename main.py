import cv2
import numpy as np

# Video source (replace 'traffic.mp4' with your traffic path or use 0 for webcam)
cap = cv2.VideoCapture('traffic.mp4')  # Replace 'traffic.mp4' with your traffic file or use 0 for live feed

# Background subtractor
bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50, detectShadows=True)

# Vehicle count and line position
vehicle_count = 0
line_y = 300  # Position of the counting line

# Function to check if a vehicle crosses the line
def is_crossing_line(y_center, line_y):
    return line_y - 5 < y_center < line_y + 5

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame for consistent processing
    frame = cv2.resize(frame, (800, 600))

    # Apply background subtraction
    fg_mask = bg_subtractor.apply(frame)

    # Remove noise using morphological operations
    kernel = np.ones((5, 5), np.uint8)
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_CLOSE, kernel)

    # Find contours
    contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Filter out small contours based on area
        if cv2.contourArea(contour) < 500:
            continue

        # Get bounding box and draw it
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Calculate the center of the bounding box
        y_center = y + h // 2

        # Check if the vehicle crosses the line
        if is_crossing_line(y_center, line_y):
            vehicle_count += 1

    # Draw the counting line
    cv2.line(frame, (0, line_y), (frame.shape[1], line_y), (0, 0, 255), 2)

    # Display vehicle count
    cv2.putText(frame, f'Count: {vehicle_count}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Show the frame
    cv2.imshow('Vehicle Detection', frame)

    # Quit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(0)  # Wait indefinitely for a key press
