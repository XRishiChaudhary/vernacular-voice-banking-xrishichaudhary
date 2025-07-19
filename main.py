import requests
import sys
from gtts import gTTS

def translate_to_bengali(text):
    url = "https://libretranslate.de/translate"
    payload = {
        "q": text,
        "source": "en",
        "target": "bn",
        "format": "text"
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()["translatedText"]

def text_to_speech(text, filename="bengali_output.mp3"):
    tts = gTTS(text=text, lang='bn')
    tts.save(filename)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        english_input = " ".join(sys.argv[1:])
    else:
        english_input = "Hello, this is a test."
    bengali_text = translate_to_bengali(english_input)
    print("Translated to Bengali:", bengali_text)
    text_to_speech(bengali_text)
