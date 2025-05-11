from flask import Flask, request, jsonify
from utils.stt import transcribe_audio
from utils.tts import speak_text
from voicebot import generate_response
import os

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def handle_voice():
    audio_file = request.files["audio"]
    user_text = transcribe_audio(audio_file)
    response_text = generate_response(user_text)
    audio_response_path = speak_text(response_text)

    return jsonify({
        "user_text": user_text,
        "response_text": response_text,
        "audio_response_path": audio_response_path
    })

if __name__ == "__main__":
    app.run(debug=True)
