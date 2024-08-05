import cv2
import face_recognition

# Access to the webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture a frame from the video
    ret, frame = video_capture.read()

    # Convert the frame to RGB (because OpenCV takes the frame as BGR)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces in the frame and their positions
    face_locations = face_recognition.face_locations(rgb_frame)

    for top, right, bottom, left in face_locations:
        # Draw a rectangle around each face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    # Display frame
    cv2.imshow('Video', frame)

    # The end of the display if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Releasing the webcam and closing all windows
video_capture.release()
cv2.destroyAllWindows()
