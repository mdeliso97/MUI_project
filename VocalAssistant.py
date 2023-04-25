import pyttsx3

class VocalAssistant(object):

    def __init__(self):

        # Takes track of the previous vocal output
        self.vocal_output = False

        # Initialize the pyttsx3 engine
        self.engine = pyttsx3.init()

        # Set the voice to use (optional)
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', 'english')
        self.engine.setProperty('rate', 180)

        self.last_command = None

    def command_respond(self, results):
        # Takes track of the previous vocal output
        global vocal_output
        vocal_output = self.engine._inLoop

        if results.multi_hand_landmarks:
            # Loop through each detected hand
            for hand_idx, hand_landmarks in enumerate(results.multi_hand_landmarks):

                if not vocal_output:
                    # Get the handness of the detected hand
                    handness = results.multi_handedness[hand_idx].classification[0].label

                    # Determine if the detected hand is a left or right hand
                    if handness == 'Left' and self.last_command != 'Left':
                        # Detected hand is a right hand, axes inverted mirrored image
                        text = "The left hand is now selected. Show me what you got!"
                        self.last_command = 'Left'
                        self.engine.say(text)
                        self.engine.runAndWait()

                    elif handness == 'Right' and self.last_command != 'Right':
                        self.last_command = 'Right'
                        text = "Selected right Hand"
                        self.engine.say(text)
                        self.engine.runAndWait()

