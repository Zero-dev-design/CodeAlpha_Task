AI LANGUAGE TRANSLATOR PROJECT
==============================

Project Name:
--------------
AI Language Translator with Text-to-Speech

Project Description:
--------------------
This project is a web-based language translation application developed using Python Flask.
The application allows users to:

- Translate text between multiple languages
- Listen to translated text using Text-to-Speech
- Copy translated text
- Pause, Continue, and Restart speech playback
- Swap source and target languages
- Use a modern responsive user interface

The project uses:
- Flask (Backend Framework)
- Deep Translator API
- Google Text-to-Speech (gTTS)
- HTML, CSS, JavaScript

------------------------------------------------------------

FEATURES
--------
1. Language Translation
2. Text-to-Speech
3. Pause/Continue Audio
4. Restart Audio
5. Copy Translation
6. Multiple Language Support
7. Responsive Modern UI
8. Language Swap Feature

------------------------------------------------------------

SUPPORTED LANGUAGES
-------------------
- English
- Hindi
- Bengali
- Marathi
- Tamil
- Telugu
- Kannada
- Malayalam
- Gujarati
- Punjabi
- Urdu
- Spanish
- French
- German
- Japanese
- Korean
- Chinese
- Russian
- Arabic

------------------------------------------------------------

TECHNOLOGIES USED
-----------------
Frontend:
- HTML
- CSS
- JavaScript

Backend:
- Python
- Flask

Libraries:
- deep-translator
- gTTS

------------------------------------------------------------

PROJECT STRUCTURE
-----------------

Language Translator/
│
├── app.py
├── requirements.txt
│
├── templates/
│     └── index.html
│
└── static/
      └── style.css

------------------------------------------------------------

INSTALLATION STEPS
------------------

1. Install Python

Download Python from:
https://www.python.org/downloads/

IMPORTANT:
Enable "Add Python to PATH" during installation.

------------------------------------------------------------

2. Install Required Libraries

Open terminal in project folder and run:

pip install flask
pip install deep-translator
pip install gtts

OR

pip install -r requirements.txt

------------------------------------------------------------

3. Run the Project

Open terminal inside project folder and run:

python app.py

------------------------------------------------------------

4. Open Browser

Open:

http://127.0.0.1:5000

------------------------------------------------------------

HOW THE PROJECT WORKS
---------------------

1. User enters text.
2. User selects source and target languages.
3. Flask backend receives input.
4. Translation API translates the text.
5. Result is displayed on screen.
6. gTTS converts translated text into speech.
7. Audio is played in browser.

------------------------------------------------------------

TEXT-TO-SPEECH FEATURES
-----------------------
- Speak translated text
- Pause speech
- Continue from paused position
- Restart speech from beginning

------------------------------------------------------------

KNOWN LIMITATIONS
-----------------
- Internet connection is required
- Some languages may take a few seconds to generate speech
- Translation accuracy depends on translation API
- Speech quality may vary for some languages

------------------------------------------------------------

FUTURE IMPROVEMENTS
-------------------
- Translation History
- User Login System
- Dark/Light Theme Toggle
- Voice Input
- Offline Translation
- Advanced AI Voices
- Export Translation as File

------------------------------------------------------------

NOTE
----
Developed as a Language Translation Tool Project using Flask and Python.

------------------------------------------------------------

AUTHOR
------
Submitted by:
Sagar Biswas (BCA Student)

Submitted for Code Alpha Tasks.

------------------------------------------------------------

END OF README
-------------
