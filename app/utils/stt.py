from faster_whisper import WhisperModel

model = WhisperModel("base")

def transcribe_audio(audio_file):
    audio_path = "./temp.wav"
    audio_file.save(audio_path)
    segments, _ = model.transcribe(audio_path)
    text = " ".join(segment.text for segment in segments)
    return text
