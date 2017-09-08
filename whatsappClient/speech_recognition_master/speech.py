import speech_recognition as sr
import os,sys,commands,signal

path = 'https://mmi211.whatsapp.net/d/GgzdWKJ6tdgHb9ifiLx01lV4TAwABRgq1nAszw/AhmqdiJdVUtX2FMeZ60eJkTekPmHys0iCV6_Z51N9PUI.amr'

commands.getoutput('wget ' + path );
fname = path.split('/')[-1];
print fname;

commands.getoutput('ffmpeg -i ' + fname + ' ' + fname.split('.')[0] + '.wav');
r = sr.Recognizer()
with sr.WavFile(fname.split('.')[0] + '.wav') as source:              # use "test.wav" as the audio source
    audio = r.record(source)                        # extract audio data from the file

try:
    print("Transcription: " + r.recognize(audio))   # recognize speech using Google Speech Recognition
except LookupError:                                 # speech is unintelligible
    print("Could not understand audio")
