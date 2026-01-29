# Import OpenCV for webcam access, image processing, and drawing
import cv2

# Import the main MediaPipe package (used for Image wrapper and enums)
import mediapipe as mp

# Import MediaPipe Tasks Python base utilities
from mediapipe.tasks import python

# Import MediaPipe vision-specific task APIs (FaceDetector, options, modes)
from mediapipe.tasks.python import vision


# -------------------- CAMERA INITIALIZATION --------------------

# Open the default webcam (index 0)
# cv2.CAP_DSHOW forces DirectShow backend for better stability on Windows
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


# -------------------- MODEL LOADING --------------------

# Create base options for MediaPipe Tasks
# Here we explicitly provide the path to the face detection model (.tflite file)
base_options = python.BaseOptions(
    model_asset_path="models/blaze_face_short_range.tflite"
)

# Configure face detector options
options = vision.FaceDetectorOptions(
    base_options=base_options,               # Attach the model configuration
    running_mode=vision.RunningMode.VIDEO    # VIDEO mode is required for live streams
)

# Create the face detector instance using the provided options
detector = vision.FaceDetector.create_from_options(options)


# -------------------- MAIN PROCESSING LOOP --------------------

# Run an infinite loop to continuously read frames from the webcam
while True:

    # Read a single frame from the webcam
    # ret indicates whether the frame was read successfully
    ret, frame = cap.read()

    # If frame capture fails, exit the loop
    if not ret:
        break

    # Flip the frame horizontally to create a mirror-like view
    frame = cv2.flip(frame, 1)

    # Convert the frame from BGR (OpenCV default) to RGB
    # MediaPipe expects images in RGB format
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Wrap the RGB NumPy array into a MediaPipe Image object
    # SRGB specifies standard RGB color space
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    # Perform face detection on the current video frame
    # detect_for_video() requires:
    # 1. MediaPipe Image object
    # 2. Timestamp in milliseconds (monotonically increasing)
    detection_result = detector.detect_for_video(
        mp_image,
        int(cv2.getTickCount() / cv2.getTickFrequency() * 1000)
    )

    # Initialize face counter for the current frame
    count = 0

    # Check if any faces were detected
    if detection_result.detections:

        # Iterate over all detected faces
        for det in detection_result.detections:
            count += 1  # Increment face count

            # Extract bounding box information for the detected face
            bbox = det.bounding_box

            # Get top-left corner coordinates of the bounding box
            x, y = bbox.origin_x, bbox.origin_y

            # Get width and height of the bounding box
            w, h = bbox.width, bbox.height

            # Draw a green rectangle around the detected face
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

    # Display the total number of faces detected on the frame
    cv2.putText(
        frame,
        f"Faces: {count}",                # Text to display
        (20, 40),                         # Position on the frame
        cv2.FONT_HERSHEY_SIMPLEX,          # Font type
        1,                                 # Font scale
        (0, 0, 255),                       # Text color (red)
        2                                  # Text thickness
    )

    # Show the processed frame in a window titled "Face Counter"
    cv2.imshow("Face Counter", frame)

    # Check if the 'q' key is pressed
    # If yes, exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# -------------------- CLEANUP --------------------

# Release the webcam resource
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
