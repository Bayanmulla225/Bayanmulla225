from gtts import gTTS
import os

text = "Hello All, This is the introduction of text to conversion using"
tts = gTTS(text=text,lang="en")
tts.save("speech.wav")