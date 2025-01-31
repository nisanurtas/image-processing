import cv2
import numpy as np

# Initialize the camera device
cap = cv2.VideoCapture(0)

# Start the loop if the camera is open
while cap.isOpened():
    ret, frame = cap.read()  # Capture frame from the camera

    if ret:
        # Define input and output points for affine transform
        rows, cols, ch = frame.shape
        src_points = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
        dst_points = np.float32([[0, 0], [int(0.6 * (cols - 1)), 0], [int(0.4 * cols - 1), rows - 1]])

        # Compute the affine transform matrix
        affine_matrix = cv2.getAffineTransform(src_points, dst_points)

        # Apply affine transform
        affine_frame = cv2.warpAffine(frame, affine_matrix, (cols, rows))

        # Display the original and transformed frames
        cv2.imshow('Original Frame', frame)
        cv2.imshow('Affine Transform Frame', affine_frame)

        # Exit the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Failed to capture frame.")
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
