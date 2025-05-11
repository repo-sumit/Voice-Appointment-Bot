from gtts import gTTS
import os

def speak_text(text):
    output_path = "./static/response.mp3"
    tts = gTTS(text)
    tts.save(output_path)
    return output_path
