import json
import os
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translate english text to french using MyMemoryTranslator.
    """
    french_text = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(english_text)
    print(french_text)
    return french_text

def french_to_english(french_text):
    """
    Translate french text to english using MyMemoryTranslator.
    """
    english_text = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(french_text)
    print(english_text)
    return english_text 

english_to_french("hello how are you")
french_to_english("bonjour comment allez-vous")