# app.py
from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_text_to_audio():
    text_to_convert = request.form['text_to_convert']
    tts = gTTS(text=text_to_convert, lang='en')
    output_file = "static/output.mp3"
    tts.save(output_file)
    return send_file(output_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
