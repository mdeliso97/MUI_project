import music21 as m21
from VocalAssistant import VocalAssistant

class loop(object):

    def __init__(self):
        self.sp = m21.midi.realtime.StreamPlayer(m21.stream.Stream())
        self.va = VocalAssistant()
        self.loop = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],]
        self.notes = ['C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2',
                'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3',
                'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4',
                'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5',
                'C6', 'D6', 'E6', 'F6', 'G6', 'A6', 'B6']
        self.recordingMode = False
    
    def add_chord(self,finger_tips):
        d = m21.duration.Duration()
        d.quarterLength = 0.1

        keys = list(finger_tips.keys())

        st2 = m21.stream.Stream()
        chord = m21.chord.Chord([m21.pitch.Pitch(self.notes[int(finger_tips[keys[index]][0] * len(self.notes))]) for index in range(len(list(finger_tips.keys())))])
        
        st2.append(chord)  

        if self.recordingMode:
            self.loop.append(chord)

        # Play the chord
        self.sp = m21.midi.realtime.StreamPlayer(st2)
        self.sp.play()

    def playLoop(self):
        st2 = m21.stream.Stream()
        for chord in self.loop:
            st2.append(chord)  

        # Play the chord
        self.sp = m21.midi.realtime.StreamPlayer(st2)
        self.sp.play()

    def stopLoop(self):
        self.sp.stop()

    def startRecord(self):
        self.va.text_to_speech("recording")
        self.recordingMode = True

