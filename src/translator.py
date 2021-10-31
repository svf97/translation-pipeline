from transformers import pipeline

# Init translator
translator = pipeline("translation_en_to_de")

# Translate text
text = "Hello my friends! How are you doing today?"
translation = translator(text)

# Print translation
print(translation)