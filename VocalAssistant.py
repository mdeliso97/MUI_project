import pyttsx3


# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set the voice to use (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set the voice to the second voice in the list


def command_respond(results):

    # Loop through each detected hand
    for hand_idx, hand_landmarks in enumerate(results.multi_hand_landmarks):

        # Get the handness of the detected hand
        handness = results.multi_handedness[hand_idx].classification[0].label

        # Determine if the detected hand is a left or right hand
        if handness == 'Left':
            # Detected hand is a left hand
            text = "Left Hand"
            engine.say(text)
            engine.runAndWait()

        elif handness == 'Right':
            # Detected hand is a right hand
            text = "Right Hand"
            engine.say(text)
            engine.runAndWait()
