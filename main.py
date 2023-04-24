import cv2
import mediapipe as mp
import music21 as m21
import threading
import multiprocessing
import VocalAssistant as va


def play_chord(finger_tips):
    d = m21.duration.Duration()
    d.quarterLength = 0.5

    # Define the pitches and duration for each finger
    notes = {mp_hands.HandLandmark.THUMB_TIP: (m21.pitch.Pitch('C3'), d),
            mp_hands.HandLandmark.INDEX_FINGER_TIP: (m21.pitch.Pitch('D3'), d),
            mp_hands.HandLandmark.MIDDLE_FINGER_TIP: (m21.pitch.Pitch('E3'), d),
            mp_hands.HandLandmark.RING_FINGER_TIP: (m21.pitch.Pitch('F3'), d),
            mp_hands.HandLandmark.PINKY_TIP: (m21.pitch.Pitch('G3'), d)}

    st2 = m21.stream.Stream()
    chord2 = m21.chord.Chord([notes[finger][0] for finger in finger_tips.keys()])
    st2.append(chord2)
    # Play the chord
    sp = m21.midi.realtime.StreamPlayer(st2)
    sp.play()


def detect_hands(cap, hands):
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:
                # Get the coordinates of the fingertips
                finger_tips = {landmark: (hand_landmarks.landmark[landmark].x,
                                          hand_landmarks.landmark[landmark].y)
                                          for landmark in
                                          [mp_hands.HandLandmark.INDEX_FINGER_TIP,
                                           mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                                           mp_hands.HandLandmark.RING_FINGER_TIP,
                                           mp_hands.HandLandmark.PINKY_TIP,
                                           mp_hands.HandLandmark.THUMB_TIP]}

                # Play chord in a separate thread
                threading.Thread(target=play_chord, args=(finger_tips,)).start()

                # Play Audio when certain manipulations are performed in a separate thread
                threading.Thread(target=va.command_respond, args=(results,)).start()

                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
            # Flip the image horizontally for a selfie-view display.
            cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
            if cv2.waitKey(5) & 0xFF == 27:
                    break
    cap.release()

if __name__ == '__main__':
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands

    cap = cv2.VideoCapture(0)
    hands = mp_hands.Hands(
        model_complexity=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5)

    detect_hands(cap, hands)
