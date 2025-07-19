from googletrans import Translator
from gtts import gTTS

# Step 1: Translate English to Bengali
def translate_to_bengali(text):
    translator = Translator()
    result = translator.translate(text, src='en', dest='bn')  # 'bn' = Bengali language code
    return result.text

# Step 2: Convert Bengali text to speech and play it
def text_to_speech(text, filename="bengali_output.mp3"):
    tts = gTTS(text=text, lang='bn')
    tts.save(filename)

# --- Main ---
if __name__ == "__main__":
    english_input = "Transferring 100 rupees from your account"
    bengali_text = translate_to_bengali(english_input)
    print("Translated to Bengali:", bengali_text)
    text_to_speech(bengali_text)
