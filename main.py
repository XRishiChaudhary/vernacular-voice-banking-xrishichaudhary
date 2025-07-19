from googletrans import Translator
from gtts import gTTS
import sys

# Step 1: Translate English to Bengali
def translate_to_bengali(text):
    translator = Translator()
    result = translator.translate(text, src='en', dest='bn')  # 'bn' = Bengali language code
    return result.text

# Step 2: Convert Bengali text to speech and save it
def text_to_speech(text, filename="bengali_output.mp3"):
    tts = gTTS(text=text, lang='bn')
    tts.save(filename)

# --- Main ---
if __name__ == "__main__":
    if len(sys.argv) > 1:
        english_input = " ".join(sys.argv[1:])
    else:
        english_input = "Hello, this is a test."  # Default for CI
    bengali_text = translate_to_bengali(english_input)
    print("Translated to Bengali:", bengali_text)
    text_to_speech(bengali_text)
