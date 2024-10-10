from googletrans import Translator

def translate_to_kannada(text):
    translator = Translator()
    translated_text = translator.translate(text, dest='kn').text
    return translated_text

# Example usage
english_text = "Hello, how are you?"
kannada_translation = translate_to_kannada(english_text)
print("English:", english_text)
print("Kannada:", kannada_translation)
