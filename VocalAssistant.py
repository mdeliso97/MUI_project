import pyttsx3


# Takes track of the previous vocal output
count_left = False
count_right = False

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set the voice to use (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set the voice to the second voice in the list


def command_respond(results):

    global count_right, count_left
    if results.multi_hand_landmarks:
        # Loop through each detected hand
        for hand_idx, hand_landmarks in enumerate(results.multi_hand_landmarks):

            # Get the handness of the detected hand
            handness = results.multi_handedness[hand_idx].classification[0].label

            # Determine if the detected hand is a left or right hand
            if handness == 'Left' and not count_right:
                # Detected hand is a right hand, axes inverted mirrored image
                text = "Selected Right Hand"
                engine.say(text)
                engine.runAndWait()
                count_right = True
                count_left = False

            elif handness == 'Right' and not count_left:
                # Detected hand is a left hand, axes inverted mirrored image
                text = "Selected Left Hand"
                engine.say(text)
                engine.runAndWait()
                count_left = True
                count_right = False
