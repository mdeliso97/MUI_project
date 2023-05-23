import music21 as m21
import time
from VocalAssistant import VocalAssistant
import threading

class loop(object):

    def __init__(self):
        self.sp = m21.midi.realtime.StreamPlayer(m21.stream.Stream())
        self.va = VocalAssistant()
        self.loop = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        self.notes = [ 'G3', 'A3', 'B3','C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4','C5', 'D5', 'E5']
        self.recordingMode = False
        self.ticker = time.time()#this may be wrong
        self.bpm = 80
        self.isPlaying = False
    
    def handle_chord(self,finger_tips):

        keys = list(finger_tips.keys())
        playedNotes =  [self.notes[int(finger_tips[keys[index]][0] * len(self.notes))] for index in range(len(list(finger_tips.keys())))]

        if self.recordingMode:
            elapsedTime = (time.time() - self.ticker)
            print("elapsedTime", elapsedTime)
            for note in playedNotes:
                self.loop[round(elapsedTime % 16)].append(note)
            print(self.loop)

        self.play_chord(playedNotes)


    def play_chord(self, notes):
        

        d = m21.duration.Duration()
        d.quarterLength = 0.1

        st2 = m21.stream.Stream()

        #make chord with notes
        #chord = m21.chord.Chord([m21.pitch.Pitch(self.notes[int(finger_tips[keys[index]][0] * len(self.notes))]) for index in range(len(list(finger_tips.keys())))])


        chord = m21.chord.Chord(notes)

        st2.append(chord)  


        # Play the chord
        self.sp = m21.midi.realtime.StreamPlayer(st2)
        self.sp.play()

    def playLoop(self):
        loopEmpty = True
        for notes in self.loop:
            if len(notes) != 0:
                loopEmpty = False
                continue

        if not loopEmpty:
            self.isPlaying = True
            self.ticker = time.time()
            while self.isPlaying:
                for chords in self.loop:
                    self.play_chord(chords)

    def stopLoop(self):
        self.isPlaying = False
        self.sp.stop()

    def startRecord(self):
        threading.Thread(target=self.va.text_to_speech, args=("recording",)).start()
        #self.va.text_to_speech("recording")
        self.recordingMode = True
        self.ticker = time.time()

    def stopRecord(self):
        threading.Thread(target=self.va.text_to_speech, args=("stopping recording",)).start()
        self.recordingMode = False
