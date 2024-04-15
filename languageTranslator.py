import urllib.request
from translate import Translator


try:
    response = urllib.request.urlopen('https://libretranslate.com')
    print("Connection successful, status:", response.status)
except urllib.error.URLError as e:
    print("Error connecting to LibreTranslate:", e.reason)

languages = ['en', 'fr', 'ar']

text = input("What text would you like to translate? >> ")

for language in languages:
    translator = Translator(provider='libre', from_lang='en', to_lang=language)
    translation = translator.translate(text)
    print(f"Translation to {language}: {translation}")