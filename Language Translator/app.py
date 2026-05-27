from flask import Flask, render_template, request, send_file
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

app = Flask(__name__)

languages = {

    "English": "en",
    "Hindi": "hi",
    "Bengali": "bn",
    "Marathi": "mr",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Urdu": "ur",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN", #    "Chinese": "zh-cn",
    "Russian": "ru",
    "Arabic": "ar"
}

translated_text = ""
current_language = "en"

@app.route("/", methods=["GET", "POST"])
def home():

    global translated_text
    global current_language

    original_text = ""

    source_lang = "en"
    target_lang = "hi"

    if request.method == "POST":

        original_text = request.form["text"]
        source_lang = request.form["source_language"]
        target_lang = request.form["target_language"]

        current_language = target_lang

        try:

            translated_text = GoogleTranslator(
                source=source_lang,
                target=target_lang
            ).translate(original_text)

        except Exception as e:

            translated_text = f"Error: {e}"

    return render_template(
        "index.html",
        languages=languages,
        translated_text=translated_text,
        original_text=original_text,
        source_lang=source_lang,
        target_lang=target_lang
    )
    
@app.route("/speak")
def speak():

    global translated_text
    global current_language

    try:

        if translated_text:

            audio_path = os.path.join(
                os.getcwd(),
                "speech.mp3"
            )

            tts = gTTS(
                text=translated_text,
                lang=current_language,
                slow=False
            )

            tts.save(audio_path)

            return send_file(
                audio_path,
                mimetype="audio/mpeg"
            )

        return "No translated text found"

    except Exception as e:

        return f"Speech Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)