import asyncio
from googletrans import Translator
from gtts import gTTS
import pygame

# Step 1: Translate English to Bengali
async def translate_to_bengali(text):
    translator = Translator()
    result = await translator.translate(text, src='en', dest='bn')  # 'bn' = Bengali language code
    return result.text

# Step 2: Convert Bengali text to speech and play it
def text_to_speech(text, filename="bengali_output.mp3"):
    tts = gTTS(text=text, lang='bn')
    tts.save(filename)
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# --- Main ---
if __name__ == "__main__":
    english_input = input("Enter your message in English: ")
    bengali_text = asyncio.run(translate_to_bengali(english_input))
    print("Translated to Bengali:", bengali_text)
    text_to_speech(bengali_text)
