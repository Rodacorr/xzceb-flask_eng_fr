"Importing text for Test"
from deep_translator import MyMemoryTranslator

def englishtofrench(englishtext):
    "Translates english to french"
    frenchtext= MyMemoryTranslator(source="en", target="fr").translate(englishtext)
    print(frenchtext)
    return frenchtext

def frenchtoenglish(frenchtext):
    "Translates french to english"
    englishtext= MyMemoryTranslator(source="fr", target="en").translate(frenchtext)
    print(englishtext)
    return englishtext
