import cv2
import pyttsx3
import mediapipe as mp
from mediapipe.python.solutions import hands


# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set the voice to use (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set the voice to the second voice in the list

# Convert text to speech
text = "Hello, how are you?"
engine.say(text)
engine.runAndWait()


def command_respond(image, hands):
    # Get output image from Mediapipe main class captured from webcam
    # Hands is the Handtracking output that Mediapipe produces

    # Convert the input image to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Run hand tracking on the input image
    results = hands.process(image)

    # Check if any hands were detected
    if results.multi_hand_landmarks:
        # Loop through each detected hand
        for hand_idx, hand_landmarks in enumerate(results.multi_hand_landmarks):

            # Get the handness of the detected hand
            handness = results.multi_handedness[hand_idx].classification[0].label

            # Determine if the detected hand is a left or right hand
            if handness == 'Left':
                text = "Left Hand"
                engine.say(text)
                engine.runAndWait()
            # Detected hand is a left hand
            # Do something with the left hand landmarks
            elif handness == 'Right':
                text = "Left Hand"
                engine.say(text)
                engine.runAndWait()
        # Detected hand is a right hand
        # Do something with the right hand landmarks
